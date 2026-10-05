from scanner.server import analyze_server


def test_server_analysis():
    result = analyze_server("https://example.com")

    assert isinstance(result, dict)
    assert "server" in result
    assert "powered_by" in result