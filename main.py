import json
import time
import threading
import websocket

from server import SyntaxHandle  # MADE BY SYNTAX X GHOSTY

def now_ms():
    return int(time.time() * 1000)

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = config["token"]
STATUS = config.get("status", "online")
ACTIVITIES = config["activities"]

current_index = 0
lock = threading.Lock()

def build_payload(activity):
    return {
        "op": 3,
        "d": {
            "since": now_ms(),
            "activities": [
                {
                    "type": activity["type"],
                    "url": activity.get("url"),
                    "session_id": "session123",
                    "timestamps": {"start": now_ms()},
                    "details": activity.get("details"),
                    "state": activity.get("state"),
                    "flags": 0,
                    
                    "assets": {
                        "large_image": activity.get("large_image"),
                        "large_text": activity.get("large_text"),
                        
                    },
                    "name": activity.get("name", "")
                }
            ],
            "status": STATUS,
            "afk": False
        }
    }
# Optional MADE BY SYNTAX
def send_heartbeat(ws, interval):
    while True:
        time.sleep(interval / 1000)
        try:
            ws.send(json.dumps({"op": 1, "d": None}))
        except Exception:
            break

def on_open(ws):
    ws.send(json.dumps({
        "op": 2,
        "d": {
            "token": TOKEN,
            "properties": {
                "$os": "Linux",
                "$browser": "Chrome",
                "$device": "browser"
            }
        }
    }))
    time.sleep(2)

    global current_index
    with lock:
        activity = ACTIVITIES[current_index]
        current_index = (current_index + 1) % len(ACTIVITIES)
    ws.send(json.dumps(build_payload(activity)))
    print(f"[✅] Initial presence sent: {activity.get('name', 'Unknown')}")

def on_message(ws, message):
    data = json.loads(message)
    if data.get("op") == 10:
        heartbeat_interval = data["d"]["heartbeat_interval"]
        threading.Thread(target=send_heartbeat, args=(ws, heartbeat_interval), daemon=True).start()

def on_error(ws, error):
    print("[❌] WebSocket error:", error)

def on_close(ws, *_):
    print("[✖] WebSocket closed. Reconnecting in 5 seconds...")
    time.sleep(5)
    run_ws()

def presence_rotator(ws):
    global current_index
    while True:
        time.sleep(45)
        with lock:
            activity = ACTIVITIES[current_index]
            current_index = (current_index + 1) % len(ACTIVITIES)
        try:
            ws.send(json.dumps(build_payload(activity)))
            print(f"[🔄] Rotated presence to: {activity.get('name', 'Unknown')}")
        except Exception as e:
            print("[❌] Failed to send rotated presence:", e)
            break

def run_ws():
    ws = websocket.WebSocketApp(
        "wss://gateway.discord.gg/?v=10&encoding=json",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    def run():
        ws.run_forever()

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

    time.sleep(5)
    presence_rotator(ws)

if __name__ == "__main__":
    SyntaxHandle()
    run_ws()
