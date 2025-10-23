# WebPyChat 🗨️

A real-time web chat application built with Python (Flask-SocketIO) backend and HTML/CSS/JavaScript frontend. Chat with others on the same network or internet connection!

## Features

- 🔄 Real-time messaging using WebSocket
- 👥 Multiple users can chat simultaneously
- 📝 Typing indicators
- 💬 Chat history for new users
- 🎨 Modern, responsive UI
- 🌐 GitHub Pages frontend support

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TheCrazy8/WebPyChat.git
cd WebPyChat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

Start the chat server:
```bash
python server.py
```

The server will start on `http://localhost:5000` by default.

### Accessing the Chat

**Option 1: Local Access**
- Open your browser and go to `http://localhost:5000`
- Enter a username and start chatting!

**Option 2: Network Access**
- Find your local IP address:
  - Windows: `ipconfig`
  - Mac/Linux: `ifconfig` or `ip addr`
- Share your IP with others on the same network
- They can access the chat at `http://YOUR_IP:5000`

**Option 3: GitHub Pages (Static Frontend)**
- Visit the GitHub Pages URL: [https://thecrazy8.github.io/WebPyChat/](https://thecrazy8.github.io/WebPyChat/)
- Enter your server URL (e.g., `http://your-server-ip:5000`)
- Enter a username and join the chat

## Project Structure

```
WebPyChat/
├── server.py              # Python backend server
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface (served by Flask)
├── docs/
│   └── index.html        # GitHub Pages frontend
└── README.md             # This file
```

## How It Works

### Backend (server.py)
- Built with Flask and Flask-SocketIO
- Handles WebSocket connections
- Manages user sessions and message broadcasting
- Stores last 100 messages for chat history
- Implements typing indicators

### Frontend
- Clean, modern UI with gradient design
- Real-time updates via Socket.IO client
- Responsive design for mobile and desktop
- Typing indicators and user count
- Connection status notifications

## Configuration

### Server Configuration

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
1. Deploy the Python server to a cloud platform (Heroku, AWS, etc.)
2. Enable GitHub Pages in repository settings
3. Users can access the static frontend via GitHub Pages
4. Users enter their server URL to connect

## Security Notes

⚠️ **Important**: This is a basic chat application for educational purposes.

For production use, consider:
- Implementing authentication
- Using HTTPS/WSS (secure WebSocket)
- Adding rate limiting
- Sanitizing user input
- Using environment variables for secrets
- Adding message persistence (database)

## Technologies Used

- **Backend**: Python, Flask, Flask-SocketIO, eventlet
- **Frontend**: HTML5, CSS3, JavaScript, Socket.IO client
- **Real-time**: WebSocket protocol

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
