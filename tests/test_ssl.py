from scanner.ssl_check import check_ssl


def test_ssl_check():
    result = check_ssl("https://example.com")

    assert isinstance(result, dict)
    assert result["hostname"] == "example.com"
    assert result["certificate_valid"] is True
    assert result["tls_version"] is not None
    assert result["cipher"] is not None