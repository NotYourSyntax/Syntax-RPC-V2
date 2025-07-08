# 🌌 Syntax RPC V2

A sleek, rotating custom Discord Rich Presence (RPC)  — complete with animated emoji assets, rotating messages, and clean status updates — all over WebSocket.  
Made with 🧠 by **Syntax X Ghosty**.

---

## ✨ Features

- 🎮 Custom Discord RPC using **WebSocket Gateway**
- 🔁 Rotates between multiple rich activities 
- 🖼️ Animated `mp:` emojis and attachments as large images
- ⚡ Lightweight Python script — no client needed
- 🌐 Optional Flask server (`server.py`) support

---

## 📦 Installation

Download The File
Extract IT 
Open the terminal 
type the command
pip install -r requirements.txt
⚙️ Configuration
Edit config.json:
{
  "token": "YOUR_DISCORD_TOKEN_HERE",
  "status": "dnd",
  "activities": [
    {
      "type": 1,
      "url": "https://www.twitch.tv/Syntax",
      "details": "! Syntax 🥀",
      "state": "Maybe a dev?",
      "large_image": "mp:emojis/1392073935243317268",
      "large_text": "Code Wizard",
      "name": "Coding Adventures"
    }
  ]
}
type: 1 = Streaming (required for Twitch-like presence)

url = Twitch stream URL (must be valid)

large_image = Use mp:emojis/<emoji_id> or mp:attachments/<channel_id>/<file_id>.gif

name, details, state = Shown in the RPC panel

Save it .
After That Type
python main.py to run
