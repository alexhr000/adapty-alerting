import requests
import json


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