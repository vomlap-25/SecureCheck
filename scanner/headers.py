import requests


SECURITY_HEADERS = {
    "Content-Security-Policy": "High",
    "Strict-Transport-Security": "High",
    "X-Content-Type-Options": "Medium",
    "X-Frame-Options": "Medium",
    "Referrer-Policy": "Low",
    "Permissions-Policy": "Low"
}


def analyze_headers(url):
    response = requests.get(url, timeout=10)

    findings = []

    for header, severity in SECURITY_HEADERS.items():
        if header in response.headers:
            findings.append({
                "header": header,
                "status": "present",
                "severity": "none"
            })
        else:
            findings.append({
                "header": header,
                "status": "missing",
                "severity": severity
            })

    return findings