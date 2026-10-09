from scanner.headers import analyze_headers
from scanner.ssl_check import check_ssl
from scanner.cookies import analyze_cookies
from scanner.server import analyze_server
from scanner.scoring import calculate_score


def scan_website(url):
    headers = analyze_headers(url)
    ssl = check_ssl(url)
    cookies = analyze_cookies(url)
    server = analyze_server(url)

    score = calculate_score(
        headers,
        ssl,
        cookies,
        server
    )

    return {
        "url": url,
        "headers": headers,
        "ssl": ssl,
        "cookies": cookies,
        "server": server,
        "score": score
    }