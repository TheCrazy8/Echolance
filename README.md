# Echolance 🗨️

A real-time web chat application with **two modes**: peer-to-peer (P2P) chat that works instantly in your browser, or traditional server-based chat with Python backend.

## ✨ NEW: P2P Mode - No Server Required!

Now you can chat **instantly** without downloading or running anything! Just visit the GitHub Pages site and start chatting.

### Two Ways to Chat

#### 🌐 P2P Mode (Recommended for Quick Use)
- **No server setup needed** - works instantly from GitHub Pages
- **No downloads required** - everything runs in your browser
- **Peer-to-peer connections** - direct browser-to-browser communication
- **Share a room ID** - friends use the same room ID to join
- **Perfect for**: Quick chats, small groups, no technical setup

👉 **[Start P2P Chat Now](https://thecrazy8.github.io/Echolance/)**

#### 🖥️ Server Mode (For Advanced Use)
- **Persistent chat history** - messages saved on server
- **More stable** - centralized connections
- **Better for larger groups** - handles more users
- **Custom deployment** - run on your own server

## Features

### P2P Mode Features
- 🌐 Browser-to-browser communication using WebRTC
- 🔒 Peer-to-peer encryption
- 🚀 Instant start - no installation required
- 🏠 Room-based chat system
- 💬 Real-time messaging
- 👥 Multiple users per room
- 📱 Works on mobile and desktop

### Server Mode Features
- 🔄 Real-time messaging using WebSocket
- 👥 Multiple users can chat simultaneously
- 📝 Typing indicators
- 💬 Chat history (last 100 messages)
- 🎨 Modern, responsive UI
- 🌐 GitHub Pages frontend support

## Quick Start

### Option 1: P2P Mode (Instant - No Setup!)

1. Visit **[https://thecrazy8.github.io/WebPyChat/](https://thecrazy8.github.io/Echolance/)**
2. Click "Start P2P Chat"
3. Enter your username and a room ID (e.g., "mychat123")
4. Share the room ID with friends
5. Start chatting!

**That's it!** No downloads, no server setup, no technical knowledge needed.

### Option 2: Server Mode (Traditional Setup)

#### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/TheCrazy8/WebPyChat.git
cd WebPyChat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

#### Running the Server

Start the chat server:
```bash
python server.py
```

The server will start on `http://localhost:5000` by default.

To find your network IP address, run:
```bash
python get_ip.py
```

#### Accessing the Chat

**Option 1: Local Access**
- Open your browser and go to `http://localhost:5000`
- Enter a username and start chatting!

**Option 2: Network Access**
- Find your local IP address:
  - Windows: `ipconfig`
  - Mac/Linux: `ifconfig` or `ip addr`
- Share your IP with others on the same network
- They can access the chat at `http://YOUR_IP:5000`

**Option 3: GitHub Pages with Server**
- Visit [https://thecrazy8.github.io/WebPyChat/](https://thecrazy8.github.io/WebPyChat/)
- Click "Connect to Server"
- Enter your server URL (e.g., `http://your-server-ip:5000`)
- Enter a username and join the chat

## Project Structure

```
WebPyChat/
├── server.py              # Python backend server
├── get_ip.py              # Helper script to find network IP
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
├── templates/
│   └── index.html        # Web interface (served by Flask)
├── docs/
│   ├── index.html        # GitHub Pages landing page
│   ├── p2p.html          # P2P chat (no server needed)
│   └── index_server.html # Server-based chat
└── README.md             # This file
```

## How It Works

### P2P Mode
- Uses **WebRTC** for direct peer-to-peer connections
- **PeerJS** library simplifies WebRTC setup
- **LocalStorage** for room peer discovery
- **No server required** - everything runs in the browser
- Encrypted browser-to-browser communication

### Server Mode

#### Backend (server.py)
- Built with Flask and Flask-SocketIO
- Handles WebSocket connections
- Manages user sessions and message broadcasting
- Stores last 100 messages for chat history
- Implements typing indicators

#### Frontend
- Clean, modern UI with gradient design
- Real-time updates via Socket.IO client
- Responsive design for mobile and desktop
- Typing indicators and user count
- Connection status notifications

## Configuration

### P2P Mode Configuration

No configuration needed! Just visit the page and start chatting.

To customize the P2P experience, you can modify `docs/p2p.html`:
- Adjust STUN servers for better connectivity
- Modify room peer discovery mechanism
- Customize UI colors and styles

### Server Mode Configuration

Edit `server.py` to customize:
- Port: Change `port=5000` in `socketio.run()`
- Host: Change `host='0.0.0.0'` to restrict access
- Secret key: Update `SECRET_KEY` for production use

### Frontend Configuration

For the Flask template (`templates/index.html`):
- No configuration needed - connects to the serving server

For the GitHub Pages version (`docs/index.html`):
- Users enter the server URL at runtime

## Deployment

### Local Network
1. Start the server on a machine accessible to your network
2. Share the server IP address with users
3. Users navigate to `http://SERVER_IP:5000`

### Public Internet

**P2P Mode (Easiest)**:
1. Enable GitHub Pages in your repository settings
2. Share the GitHub Pages URL with users
3. No server deployment needed!

**Server Mode**:
1. Deploy the Python server to a cloud platform (Heroku, AWS, etc.)
2. Enable GitHub Pages in repository settings
3. Users can access the static frontend via GitHub Pages
4. Users enter their server URL to connect

## Security Notes

⚠️ **Important**: This is a basic chat application for educational purposes.

### P2P Mode Security
- WebRTC provides encrypted peer-to-peer connections
- No data passes through a central server
- Room IDs stored in browser LocalStorage
- Suitable for casual, non-sensitive conversations

### Server Mode Security
For production use, consider:
- Implementing authentication
- Using HTTPS/WSS (secure WebSocket)
- Adding rate limiting
- Sanitizing user input
- Using environment variables for secrets
- Adding message persistence (database)

## Technologies Used

### P2P Mode
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **P2P Library**: PeerJS 1.5.2 (WebRTC wrapper)
- **WebRTC**: For peer-to-peer connections
- **LocalStorage**: For room peer discovery

### Server Mode
- **Backend**: Python 3.7+, Flask 3.0.0, Flask-SocketIO 5.3.5
- **Frontend**: HTML5, CSS3, JavaScript, Socket.IO client 4.5.4
- **Real-time**: WebSocket protocol with threading async mode

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Connection Issues
- Ensure the server is running
- Check firewall settings
- Verify the correct IP/port is being used

### Port Already in Use
- Change the port in `server.py`
- Or stop the process using port 5000

### Dependencies Not Installing
- Upgrade pip: `pip install --upgrade pip`
- Use virtual environment: `python -m venv venv`

## Contact

For issues, questions, or suggestions, please open an issue on GitHub.
