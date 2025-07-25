# 🎮 Smash Karts Bot - Render.com Edition

A cloud-powered Smash Karts bot that runs on Render.com, keeping your PC cool while the bot plays automatically!

## 🌟 Features

- **Cloud-powered**: Runs on Render.com servers, no local resources used
- **Web Dashboard**: Beautiful web interface to control your bot
- **Real-time Status**: Monitor bot status, cycles, and uptime
- **No Heat**: Your PC stays cool while the bot runs remotely
- **Easy Control**: Start, stop, and monitor from any device

## 🚀 Quick Deploy to Render.com

### Option 1: One-Click Deploy (Recommended)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy/schema/new?template=https://github.com/yourusername/smash-karts-bot)

### Option 2: Manual Deploy

1. **Fork this repository** to your GitHub account

2. **Sign up for Render.com** (free tier available)

3. **Create a new Web Service**:
   - Connect your GitHub repository
   - Choose the repository you just forked
   - Set the following:
     - **Name**: `smash-karts-bot`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python render_bot_app.py`

4. **Deploy!** Render will automatically build and deploy your bot

## 🎯 How to Use

1. **Access your bot**: Once deployed, visit your Render.com URL (e.g., `https://your-bot-name.onrender.com`)

2. **Setup the bot**: Click "Setup Bot" to initialize the browser and load the game

3. **Start playing**: Click "Start Bot" to begin the automated gameplay

4. **Monitor progress**: Watch the real-time status, cycle count, and uptime

5. **Stop when done**: Click "Stop Bot" to end the session

## 📊 Dashboard Features

- **Real-time Status**: See if the bot is idle, loading, or running
- **Cycle Counter**: Track how many movement cycles completed
- **Uptime Timer**: Monitor how long the bot has been running
- **Live Logs**: View real-time activity logs
- **One-click Controls**: Easy setup, start, stop, and cleanup

## 🔧 Technical Details

### Bot Movement Pattern
The bot follows a complex movement pattern:
1. Forward (5 seconds)
2. Forward + Left (5 seconds)
3. Forward + Right (5 seconds)
4. Jump
5. Backward (5 seconds)
6. Backward + Left (5 seconds)
7. Backward + Right (5 seconds)
8. Jump
9. Repeat

### Cloud Infrastructure
- **Render.com**: Hosts the web application and bot
- **Chrome Headless**: Runs the game without GUI
- **Flask Web Server**: Provides the control interface
- **Selenium WebDriver**: Automates browser interactions

## 🛠️ Local Development

If you want to run locally for testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python render_bot_app.py

# Visit http://localhost:5000
```

## 📁 Project Structure

```
smash-karts-bot/
├── render_bot_app.py      # Main Flask application
├── templates/
│   └── dashboard.html     # Web dashboard
├── requirements.txt       # Python dependencies
├── render.yaml           # Render.com configuration
├── Dockerfile            # Docker configuration
└── README.md            # This file
```

## 🔒 Security Notes

- The bot runs in a sandboxed environment on Render.com
- No personal data is stored or transmitted
- The web interface is public - anyone with the URL can control the bot
- Consider adding authentication if needed for production use

## 💡 Tips

1. **Free Tier Limits**: Render.com free tier has usage limits. The bot will sleep after 15 minutes of inactivity.

2. **Game Loading**: The game may take a few seconds to load initially.

3. **Network Stability**: Ensure stable internet connection for the bot to work properly.

4. **Browser Compatibility**: The bot is optimized for Chrome on Render.com servers.

## 🐛 Troubleshooting

### Bot won't start
- Check if the game loaded properly
- Ensure the browser setup completed successfully
- Check the logs for error messages

### Game not loading
- The game might be temporarily unavailable
- Try the setup process again
- Check your internet connection

### Render deployment issues
- Ensure all files are committed to your repository
- Check the build logs in Render dashboard
- Verify Python version compatibility

## 📄 License

This project is for educational purposes. Please respect the game's terms of service.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Enjoy your cool PC while the bot plays Smash Karts in the cloud! 🎮❄️** #   a u t o s m a s h e r  
 #   r e n d e r a u t o s m a s h  
 