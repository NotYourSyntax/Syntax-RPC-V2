# 🌌 Syntax RPC V2

A sleek, rotating custom Discord Rich Presence (RPC) — complete with animated emoji assets, rotating messages, and clean status updates — all over WebSocket.  
Made with 🧠 by Syntax X Ghosty.

---

## ✨ Features

- 🎮 Custom Discord RPC using WebSocket Gateway  
- 🔁 Rotates between multiple rich activities  
- 🖼️ Animated `mp:` emojis and attachments as large images  
- ⚡ Lightweight Python script — no Discord client needed  
- 🌐 Optional Flask server (`server.py`) support  

---

## 📦 Installation

1. Download the repository files and extract them.  
2. Open your terminal and run:  
   ```bash
   pip install -r requirements.txt
## ⚙️ Configuration

Create or edit `config.json` file with the following content (replace the token with your own Discord token):

```json
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
    },
    {
      "type": 1,
      "url": "https://www.twitch.tv/Syntax",
      "details": "I Love Athy <3",
      "state": "She is mine",
      "large_image": "mp:attachments/1388263094500724840/1391844826202374224/lylies.gif",
      "large_text": "Syntax Love Athy",
      "name": "Syntax X Athy"
    },
    {
      "type": 1,
      "url": "https://www.twitch.tv/Syntax",
      "details": "Syntax Rulez Cord",
      "state": "Exploiting 1007",
      "large_image": "mp:attachments/1388263094500724840/1391844711291031573/1.gif",
      "large_text": "Be aware",
      "name": "Syntax On Top"
    }
  ]
} 
```

## 🚀 Run

Run the main script with:

```bash
python main.py
Made with 🧠 by Syntax X Ghosty.
Enjoy your custom rotating Discord presence! 🎉

👤 Author
GhoSty X SynTax | [ Async Development ]
Discord: @ghostyjija @terrifiying
Support Server: Join Here

🤝 Contributing
Contributions, issue reports, and feature suggestions are welcome!
Feel free to join our Discord community for discussions and support.

⚠️ Important Notices
🚫 Re-Selling or Re-distributing this code will result in a ban.
⚠️ Use this project responsibly. The author is not responsible for any misuse or violations of Discord's Terms of Service.
