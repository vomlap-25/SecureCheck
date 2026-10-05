from scanner.cookies import analyze_cookies


def test_cookie_analysis():
    results = analyze_cookies("https://example.com")

    assert isinstance(results, list)