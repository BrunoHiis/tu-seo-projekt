import requests
import sys


def check_website(url, user_agent):
    try:
        request = requests.get(
            url, headers={
                'User-Agent': user_agent,
                'From': 'test@test.com'
            })

        if request.status_code == 200:
            return True
        else:
            return False
    except:
        print("Could not get data! Confirm that you entered a valid URL. Closing...")
        exit()
