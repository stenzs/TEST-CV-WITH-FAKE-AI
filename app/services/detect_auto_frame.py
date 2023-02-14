import requests


def request_detecting(image_string):
    url = "http://fake_ai:80/detect_auto"
    body = {"image_string": image_string}
    requests.post(url, json=body)
