from config.logger import sync_send_msg_to_telegram
from config.config import SUBSCRIPTIONS_CHAT_ID, SUBSCRIPTIONS_BOT_API_TOKEN, games
from datetime import datetime
import requests
import schedule
import json
import time
import os





def get_report_subscriptions_per_duration(period_unit: str, start_date: str, end_date: str, api_key: str, duration: str, chart_id: str):
    url = "https://api-admin.adapty.io/api/v1/client-api/metrics/analytics/"
    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "chart_id": chart_id,
        "filters": {
            "date": [start_date, end_date],
             "duration": [duration]
        },
        "period_unit": period_unit,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data)) 
    result = response.json()   
    value = result["data"]["common"]["value"]

    return round(value)


def check_subscriptions_count(api_key,duration,chart_id):
    today_str = datetime.today().strftime('%Y-%m-%d')
    subscriptions_count = get_report_subscriptions_per_duration("day", today_str, today_str, api_key, duration, chart_id)

    return subscriptions_count



def record_subscriptions_count(duration, chart_id):
    if os.path.exists("subscriptions_data.json"):
        with open("subscriptions_data.json", "r") as json_file:
            try:
                previous_data = json.load(json_file)
            except json.JSONDecodeError:
                previous_data = {}
    else:
        previous_data = {}

    subscriptions_data = previous_data.copy()

    for game_name, api_key in games.items():
        subscriptions_count = check_subscriptions_count(api_key, duration, chart_id)

        if game_name not in subscriptions_data:
            subscriptions_data[game_name] = {}

        if chart_id not in subscriptions_data[game_name]:
            subscriptions_data[game_name][chart_id] = {"duration": {}}

        previous_count = subscriptions_data[game_name][chart_id]["duration"].get(duration)
        subscriptions_data[game_name][chart_id]["duration"][duration] = subscriptions_count

        if previous_count is None:
            with open("subscriptions_data.json", "w") as json_file:
                json.dump(subscriptions_data, json_file, indent=4)
        elif previous_count != subscriptions_count:
            print(f"{game_name} {previous_count} {subscriptions_count}")
            if subscriptions_count != 0:
                match chart_id:
                    case "subscriptions_new":
                        sync_send_msg_to_telegram(f"🎉 {game_name}: new {duration} subscriber!", bot_token = SUBSCRIPTIONS_BOT_API_TOKEN, chat_id = SUBSCRIPTIONS_CHAT_ID)
                    case "subscriptions_renewal_cancelled":
                        sync_send_msg_to_telegram(f"💔 {game_name}: {duration} subscription cancelled", bot_token = SUBSCRIPTIONS_BOT_API_TOKEN, chat_id = SUBSCRIPTIONS_CHAT_ID)
                    case "refund_events":
                        sync_send_msg_to_telegram(f"🫴 {game_name}: {duration} refund", bot_token = SUBSCRIPTIONS_BOT_API_TOKEN, chat_id = SUBSCRIPTIONS_CHAT_ID)
                    case _:
                        sync_send_msg_to_telegram(f"{game_name}: {duration} {chart_id}", bot_token = SUBSCRIPTIONS_BOT_API_TOKEN, chat_id = SUBSCRIPTIONS_CHAT_ID)

            with open("subscriptions_data.json", "w") as json_file:
                json.dump(subscriptions_data, json_file, indent=4)


def check_subscriptions():
    durations = ["Weekly", "Monthly"]
    chart_ids = ["subscriptions_new", "subscriptions_renewal_cancelled", "refund_events"]

    for duration in durations:
        for chart_id in chart_ids:
            record_subscriptions_count(duration, chart_id)

# schedule.every(1).minute.do(check_subscriptions)

# while True:
#     schedule.run_pending()
#     time.sleep(1)