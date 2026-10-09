
def calculate_score(headers, ssl, cookies, server):
    score = 100

    # Headers
    for header in headers:
        if header["status"] == "missing":
            severity=header["severity"].lower()
            if severity== "high":
                score -= 15
            elif severity == "medium":
                score -= 10
            elif severity == "low":
                score -= 5

    # SSL
    if not ssl.get("certificate_valid"):
        score -= 25

    # Cookies
    for cookie in cookies:
        if not cookie.get("secure"):
            score -= 10

        if not cookie.get("httponly"):
            score -= 10

    # Server information
    if server.get("server"):
        score -= 5

    if server.get("powered_by"):
        score -= 5

    return max(score, 0)