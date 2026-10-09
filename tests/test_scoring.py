
from scanner.scoring import calculate_score


def test_calculate_score():
    headers = [
        {
            "header": "Content-Security-Policy",
            "status": "present",
            "severity": "High"
        },
        {
            "header": "Strict-Transport-Security",
            "status": "present",
            "severity": "High"
        }
    ]

    ssl = {
        "certificate_valid": True
    }

    cookies = []

    server = {
        "server": None,
        "powered_by": None
    }

    score = calculate_score(headers, ssl, cookies, server)

    assert score == 100
    assert isinstance(score, int)
    assert 0 <= score <= 100