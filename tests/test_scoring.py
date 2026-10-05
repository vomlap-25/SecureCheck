from scanner.scoring import calculate_score


def test_calculate_score():
    headers = {
        "strict_transport_security": True,
        "content_security_policy": True
    }

    ssl = {
        "valid": True
    }

    cookies = {
        "secure": True,
        "httponly": True
    }

    server = {
        "server": None,
        "powered_by": None
    }

    score = calculate_score(headers, ssl, cookies, server)

    assert score == 100
    assert isinstance(score, int)