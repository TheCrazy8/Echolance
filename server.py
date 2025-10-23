#!/usr/bin/env python3
"""
WebPyChat - A simple web-based chat application
"""
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'webpychat-secret-key-change-in-production'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Store active users
active_users = {}
# Store chat history (last 100 messages)
chat_history = []
MAX_HISTORY = 100


@app.route('/')
def index():
    """Serve the chat interface"""
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    """Handle new client connections"""
    print(f'Client connected: {request.sid}')
    # Send chat history to newly connected client
    emit('chat_history', {'messages': chat_history})


@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnections"""
    sid = request.sid
    if sid in active_users:
        username = active_users[sid]
        del active_users[sid]
        print(f'Client disconnected: {sid} (username: {username})')
        # Notify all users about disconnection
        socketio.emit('user_left', {
            'username': username,
            'count': len(active_users)
        })
    else:
        print(f'Client disconnected: {sid}')


@socketio.on('join')
def handle_join(data):
    """Handle user joining the chat"""
    username = data.get('username', 'Anonymous')
    sid = request.sid
    active_users[sid] = username
    
    print(f'User joined: {username} (sid: {sid})')
    
    # Send welcome message to the user
    emit('joined', {
        'username': username,
        'count': len(active_users)
    })
    
    # Notify all other users
    socketio.emit('user_joined', {
        'username': username,
        'count': len(active_users)
    }, skip_sid=sid)


@socketio.on('message')
def handle_message(data):
    """Handle incoming chat messages"""
    sid = request.sid
    username = active_users.get(sid, 'Anonymous')
    message = data.get('message', '')
    
    if not message.strip():
        return
    
    print(f'Message from {username}: {message}')
    
    # Create message object
    msg_obj = {
        'username': username,
        'message': message,
        'timestamp': datetime.now().isoformat()
    }
    
    # Add to history
    chat_history.append(msg_obj)
    if len(chat_history) > MAX_HISTORY:
        chat_history.pop(0)
    
    # Broadcast message to all clients
    socketio.emit('message', {
        'username': username,
        'message': message
    })


@socketio.on('typing')
def handle_typing(data):
    """Handle typing indicators"""
    sid = request.sid
    username = active_users.get(sid, 'Anonymous')
    is_typing = data.get('typing', False)
    
    # Broadcast typing status to all other clients
    socketio.emit('typing', {
        'username': username,
        'typing': is_typing
    }, skip_sid=sid)


if __name__ == '__main__':
    print('Starting WebPyChat server...')
    print('Access the chat at: http://localhost:5000')
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
