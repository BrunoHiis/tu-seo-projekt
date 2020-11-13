import requests


def check_https(url):
    request = requests.get(url)
    if "https://" in request.url:
        return True
    else:
        return False
