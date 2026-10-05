
from scanner.headers import analyze_headers
from scanner.ssl_check import analyze_ssl
from scanner.cookies import analyze_cookies
from scanner.server import analyze_server
from scanner.scoring import calculate_score


def run_scan(url):
    headers = analyze_headers(url)
    ssl = analyze_ssl(url)
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


if __name__ == "__main__":
    url = input("Enter URL: ")

    result = run_scan(url)

    print("\n=== SecureCheck Security Report ===")
    print("URL:", result["url"])
    print("Security Score:", result["score"])

    print("\nHeaders:")
    print(result["headers"])

    print("\nSSL:")
    print(result["ssl"])

    print("\nCookies:")
    print(result["cookies"])

    print("\nServer:")
    print(result["server"])
