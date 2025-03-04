from config.config import METEOR_BOT_API_TOKEN, METEOR_CHAT_ID
import threading
import requests
import logging

file_lock = threading.Lock()

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO) 
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


def sync_send_msg_to_telegram(msg, parse_mode="HTML", bot_token = METEOR_BOT_API_TOKEN, chat_id = METEOR_CHAT_ID): 
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    data = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": parse_mode 
    }

    requests.post(url, data=data)