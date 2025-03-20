from src.utils.validation import validate_country


def test_validate_country():
    assert validate_country('DE') == True
    assert validate_country('RU') == True
    assert validate_country('FR') == True
    assert validate_country('US') == True
    assert validate_country('QWE') == False
    assert validate_country('') == False
    assert validate_country('IDDQD') == False