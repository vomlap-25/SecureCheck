import socket
import ssl
from urllib.parse import urlparse


def check_ssl(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    if not hostname:
        raise ValueError("Invalid URL")

    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_socket:
            certificate = secure_socket.getpeercert()

            return {
                "hostname": hostname,
                "tls_version": secure_socket.version(),
                "certificate_valid": bool(certificate),
                "cipher": secure_socket.cipher()[0]
            }           