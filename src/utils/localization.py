import gettext
import pycountry

def localized_country(country_obj, locale: str):
    """Fetch localized name for country."""
    try:
        t = gettext.translation('iso3166-1', pycountry.LOCALES_DIR, languages=[locale])
        t.install()

        return t.gettext(country_obj.name)  # Translate country name
    except FileNotFoundError:
        return country_obj.name

def localized_official_name(country_obj, locale: str):
    """Fetch localized official name for country, fallback to common name if not available."""
    official_name = getattr(country_obj, 'official_name', None)

    if official_name:
        try:
            t = gettext.translation('iso3166-1', pycountry.LOCALES_DIR, languages=[locale])
            t.install()

            return t.gettext(official_name)
        except FileNotFoundError:
            return official_name

    return localized_country(country_obj, locale)

def localized_subdivision(subdivision_obj, locale: str):
    """Fetch localized name for subdivision."""
    try:
        t = gettext.translation('iso3166-2', pycountry.LOCALES_DIR, languages=[locale])
        t.install()

        return t.gettext(subdivision_obj.name)
    except FileNotFoundError:
        return subdivision_obj.name