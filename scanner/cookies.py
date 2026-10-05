import requests


def analyze_cookies(url):
    response = requests.get(url, timeout=10)

    findings = []

    for cookie in response.cookies:
        findings.append({
            "name": cookie.name,
            "secure": cookie.secure,
            "httponly": cookie.has_nonstandard_attr("HttpOnly"),
            "samesite": cookie.get_nonstandard_attr("SameSite")
        })

    return findings