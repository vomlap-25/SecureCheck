def calculate_score(headers, ssl, cookies, server):
    score = 100

    # Headers
    if not headers.get("strict_transport_security"):
        score -= 15

    if not headers.get("content_security_policy"):
        score -= 15

    # SSL
    if not ssl.get("valid"):
        score -= 25

    # Cookies
    if not cookies.get("secure"):
        score -= 10

    if not cookies.get("httponly"):
        score -= 10

    # Server information
    if server.get("server"):
        score -= 5

    if server.get("powered_by"):
        score -= 5

    return max(score, 0)