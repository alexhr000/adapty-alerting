from dotenv import load_dotenv
import os

load_dotenv()


METEOR_CHAT_ID = os.getenv('METEOR_CHAT_ID')
METEOR_BOT_API_TOKEN = os.getenv('METEOR_BOT_API_TOKEN')
SUBSCRIPTIONS_CHAT_ID = os.getenv('SUBSCRIPTIONS_CHAT_ID')
SUBSCRIPTIONS_BOT_API_TOKEN = os.getenv('SUBSCRIPTIONS_BOT_API_TOKEN')
AI_GAME_CHAT_API_KEY = os.getenv('AI_GAME_CHAT_API_KEY')
AI_DUB_API_KEY = os.getenv('AI_DUB_API_KEY')
AI_BLUETOOTH_API_KEY = os.getenv('AI_BLUETOOTH_API_KEY')
AI_FOLDER_API_KEY = os.getenv('AI_FOLDER_API_KEY')
AI_MUSIC_API_KEY = os.getenv('AI_MUSIC_API_KEY')

games = {
    "AI Game Chat": AI_GAME_CHAT_API_KEY,
    "AI Bluetooth": AI_BLUETOOTH_API_KEY,
    "AI Folder": AI_FOLDER_API_KEY,
    "AI Music": AI_MUSIC_API_KEY
}



