import requests
from datetime import datetime
import pytz
import os
IST=pytz.timezone("Asia/kolkata")
raw_TS=datetime.now(IST)
cur_date=raw_TS.strftime("%d-%m-%y")
cur_time=raw_TS.strftime("%H:%M:%S")
telegram_auth_token=os.environ['token']
telegram_group_id=os.environ['group_id']
msg=f"  Message received on {cur_date} at {cur_time}"
def send_msg_on_telegram(message):
    telegram_api_url=f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    tel_res=requests.get(telegram_api_url)
    if tel_res.status_code==200:
        print("INFO: Notification has been sent on telegram")
    else:
        print("ERROR: Could not send Message")
send_msg_on_telegram(msg)
