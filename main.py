from adapty_reports import get_report_installs, get_report_subscriptions_active, get_report_subscriptions_new, get_report_revenue, get_report_trials_new, get_report_trials_renewal_cancelled, get_report_refund_events, get_report_refund_money
from config.logger import sync_send_msg_to_telegram
from subscriptions import check_subscriptions
from datetime import datetime, timedelta
from config.config import games
import schedule
import time
import pytz

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

schedule.every(1).minute.do(check_subscriptions)

while True:
    schedule.run_pending()
    time.sleep(1)