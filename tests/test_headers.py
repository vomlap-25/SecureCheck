from scanner.headers import analyze_headers


def test_header_analysis():
    results = analyze_headers("https://example.com")

    assert isinstance(results, list)
    assert len(results) == 6