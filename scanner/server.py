import requests


def analyze_server(url):
    response = requests.get(url, timeout=10)

    server = response.headers.get("Server")
    powered_by = response.headers.get("X-Powered-By")

    return {
        "server": server,
        "powered_by": powered_by
    }