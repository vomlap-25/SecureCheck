from scanner.scanner import scan_website


def print_report(result):
    print("\n" + "=" * 45)
    print("           SECURECHECK REPORT")
    print("=" * 45)

    print(f"\nTarget: {result['url']}")
    print(f"Security Score: {result['score']}/100")

    print("\n--- SECURITY HEADERS ---")

    for header in result["headers"]:
        status = header["status"]
        name = header["header"]

        if status == "present":
            print(f"[+] {name}: Present")
        else:
            print(f"[-] {name}: Missing ({header['severity']})")

    print("\n--- SSL / TLS ---")

    ssl_data = result["ssl"]

    print(f"Hostname: {ssl_data['hostname']}")
    print(f"TLS Version: {ssl_data['tls_version']}")
    print(f"Certificate Valid: {ssl_data['certificate_valid']}")
    print(f"Cipher: {ssl_data['cipher']}")

    print("\n--- COOKIES ---")

    if result["cookies"]:
        for cookie in result["cookies"]:
            print(f"Cookie: {cookie['name']}")
            print(f"  Secure: {cookie['secure']}")
            print(f"  HttpOnly: {cookie['httponly']}")
            print(f"  SameSite: {cookie['samesite']}")
    else:
        print("No cookies detected.")

    print("\n--- SERVER INFORMATION ---")

    server = result["server"]

    print(f"Server: {server['server']}")
    print(f"X-Powered-By: {server['powered_by']}")

    print("\n" + "=" * 45)


if __name__ == "__main__":
    url = input("Enter website URL: ")

    result = scan_website(url)

    print_report(result)