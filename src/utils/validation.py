import pycountry


def validate_country(code: str):
    """Check if a country code is valid."""
    country = pycountry.countries.get(alpha_2=code.upper())

    return country is not None
