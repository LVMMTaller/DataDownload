import requests

def consumeApi(urlPath):
    dataResponse = requests.get(urlPath)
    if (dataResponse.status_code != 200):
        return None
    return dataResponse.text