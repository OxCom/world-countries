import logging
from fastapi import FastAPI, HTTPException, Path, Query
import pycountry
from pydantic import BaseModel

from utils.validation import validate_country
from utils.localization import localized_country, localized_official_name, localized_subdivision

app = FastAPI(title="Countries API")
logger = logging.getLogger('uvicorn.error')


class CountryModel(BaseModel):
    name: str
    alpha_2: str
    alpha_3: str
    numeric: str
    official_name: str


class SubdivisionModel(BaseModel):
    name: str
    code: str
    type: str


class CountryDetailsModel(BaseModel):
    name: str
    alpha_2: str
    alpha_3: str
    numeric: str
    official_name: str
    subdivisions: list[SubdivisionModel]


@app.get("/")
async def hello_world():
    return {"message": "Welcome to the Countries API!"}


@app.get("/countries", response_model=list[CountryModel])
async def countries(
        lang: str = Query('en', regex=r'^[a-zA-Z-]+$')
):
    logger.debug(f"GET /countries lang={lang}")

    try:
        countries = [
            CountryModel(
                name=localized_country(country, lang),
                alpha_2=country.alpha_2,
                alpha_3=country.alpha_3,
                numeric=country.numeric,
                official_name=localized_official_name(country, lang),
            )
            for country in pycountry.countries
        ]

        return countries
    except Exception as e:
        logger.error(f"Unable to handle request: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/countries/{country}", response_model=CountryDetailsModel)
async def countries(
        country: str = Path(pattern=r'^[A-Za-z]{2}$'),
        lang: str = Query('en', regex=r'^[a-zA-Z-]+$')
):
    logger.debug(f"GET /countries/{country} lang={lang}")

    if (validate_country(country) is not True):
        raise HTTPException(status_code=400, detail=f"Country code '{country}' is not supported.")

    try:
        subdivisions = [
            SubdivisionModel(
                name=localized_subdivision(subdivision, lang),
                code=subdivision.code,
                type=subdivision.type
            )
            for subdivision in pycountry.subdivisions if subdivision.country_code == country.upper()
        ]

        country_obj = pycountry.countries.get(alpha_2=country.upper())

        return CountryDetailsModel(
            name=localized_country(country_obj, lang),
            alpha_2=country_obj.alpha_2,
            alpha_3=country_obj.alpha_3,
            numeric=country_obj.numeric,
            official_name=localized_official_name(country_obj, lang),
            subdivisions=subdivisions
        )
    except Exception as e:
        logger.error(f"Unable to handle request: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/countries/{country}/subdivisions", response_model=list[SubdivisionModel])
async def subdivisions(
        country: str = Path(pattern=r'^[A-Za-z]{2}$'),
        lang: str = Query('en', regex=r'^[a-zA-Z-]+$')
):
    logger.debug(f"GET /countries/{country}/subdivisions lang={lang}")

    if (validate_country(country) is not True):
        raise HTTPException(status_code=400, detail=f"Country code '{country}' is not supported.")

    try:
        subdivisions = [
            SubdivisionModel(
                name=localized_subdivision(subdivision, lang),
                code=subdivision.code,
                type=subdivision.type
            )
            for subdivision in pycountry.subdivisions if subdivision.country_code == country.upper()
        ]

        if not subdivisions:
            raise ValueError

        return subdivisions
    except ValueError:
        raise HTTPException(status_code=404, detail="No subdivisions found for this country code")
