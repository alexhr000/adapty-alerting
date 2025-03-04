from datetime import datetime, timedelta
import requests
import json
from config.config import AI_GAME_CHAT_API_KEY,AI_DUB_API_KEY,AI_BLUETOOTH_API_KEY,AI_FOLDER_API_KEY,AI_MUSIC_API_KEY
from config.logger import sync_send_msg_to_telegram
import schedule
import time
from datetime import datetime, timedelta
import pytz


def get_report_subscriptions_new(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "subscriptions_new",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()
    
    value = result["data"]["common"]["value"]
    description = "First-time activated subscriptions"
    msg = f"{description}: {round(value)}\n"
    return msg

def get_report_revenue(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "revenue",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    
    result = response.json()
    
    value1 = result["data"]["revenue"]["value"]
    value2 = result["data"]["net_revenue"]["value"]
    description1 = "Revenue"
    description2 = "Net revenue"
    msg = f"{description1}: {value1}$\n{description2}: {value2}$\n"
    return msg


def get_report_subscriptions_active(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "subscriptions_active",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()

    value = result["data"]["common"]["value"]
    description = "Active subscriptions (excluding trials)"
    msg = f"{description}: {round(value)}\n"
    return msg


def get_report_trials_new(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "trials_new",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()

    value = result["data"]["common"]["value"]
    description = "Trials new"
    msg = f"{description}: {round(value)}\n"
    return msg

def get_report_trials_renewal_cancelled(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "trials_renewal_cancelled",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()

    value = result["data"]["common"]["value"]
    description = "Trials renewal cancelled"
    msg = f"{description}: {round(value)}\n"
    return msg


def get_report_refund_events(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "refund_events",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()

    value = result["data"]["common"]["value"]
    description = "Refund events"
    msg = f"{description}: {round(value)}\n"
    return msg

def get_report_refund_money(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "refund_money",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    value = result["data"]["revenue"]["value"]
    description = "Refund money"
    msg = f"{description}: {value}$\n"
    return msg

def get_report_installs(period_unit: str, start_date: str, end_date: str, api_key: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": "installs",
        "filters": {
            "date": [start_date, end_date],
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()

    value = result["data"]["common"]["value"]
    description = "Installs"
    msg = f"{description}: {round(value)}\n"
    return msg

def get_report(period_unit,start_date,end_date, game_name, api_key):
    if(period_unit!="day"):
        msg = f"<b>🟣Adapty {game_name} {period_unit}ly ({datetime.strptime(start_date, '%Y-%m-%d').strftime('%d.%m.%Y')} - {datetime.strptime(end_date, '%Y-%m-%d').strftime('%d.%m.%Y')}) report: </b>\n"
    else:
        msg = f"<b>🟣Adapty {game_name} daily ({datetime.strptime(start_date,'%Y-%m-%d').strftime('%d.%m.%Y')}) report: </b>\n"
    msg += get_report_installs(period_unit, start_date, end_date, api_key)
    msg += get_report_subscriptions_active(period_unit, start_date, end_date, api_key)
    msg += get_report_subscriptions_new(period_unit, start_date, end_date, api_key)
    msg += get_report_revenue(period_unit, start_date, end_date, api_key)
    msg += get_report_trials_new(period_unit, start_date, end_date, api_key)
    msg += get_report_trials_renewal_cancelled(period_unit, start_date, end_date, api_key)
    msg += get_report_refund_events(period_unit, start_date, end_date, api_key)
    msg += get_report_refund_money(period_unit, start_date, end_date, api_key)
    return msg


moscow_tz = pytz.timezone("Europe/Moscow")
today = datetime.today()
today_str = datetime.today().strftime('%Y-%m-%d')
start_of_week = (today - timedelta(days=today.weekday() + 7)).strftime('%Y-%m-%d')
end_of_week = (today - timedelta(days=today.weekday() + 1)).strftime('%Y-%m-%d')
start_of_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1).strftime('%Y-%m-%d')
end_of_month = (today.replace(day=1) - timedelta(days=1)).strftime('%Y-%m-%d')

games = {
    "AI Game Chat": AI_GAME_CHAT_API_KEY,
    "AI DUB": AI_DUB_API_KEY,
    "AI Bluetooth": AI_BLUETOOTH_API_KEY,
    "AI Folder": AI_FOLDER_API_KEY,
    "AI Music": AI_MUSIC_API_KEY
}

def daily_job():
    for key, value in games.items():
        sync_send_msg_to_telegram(get_report("day", today_str, today_str, key, value))

        
def weekly_job():
    for key, value in games.items():
        sync_send_msg_to_telegram(get_report("week",start_of_week,end_of_week, key, value))

        
def monthly_job():
    now = datetime.now(moscow_tz)
    if now.day == 1:  
        for key, value in games.items():
            sync_send_msg_to_telegram(get_report("month",start_of_month,end_of_month, key, value))

schedule.every().day.at("14:00").do(daily_job)
schedule.every().monday.at("14:00").do(weekly_job)
schedule.every().day.at("14:00").do(monthly_job)

while True:
    schedule.run_pending()
    time.sleep(1)