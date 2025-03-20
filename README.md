# World countries
The small service to provide API on top of Python [pycountry](https://github.com/pycountry/pycountry) library

## Example

List of countries
```bash
curl -D- "http://127.0.0.1:8123/countries"

HTTP/1.1 200 OK
date: Thu, 20 Mar 2025 10:14:18 GMT
server: uvicorn
content-length: 27211
content-type: application/json

[
    ...
    {"name":"Northern Mariana Islands","alpha_2":"MP","alpha_3":"MNP","numeric":"580","official_name":"Commonwealth of the Northern Mariana Islands"},
    ...
    {"name":"Qatar","alpha_2":"QA","alpha_3":"QAT","numeric":"634","official_name":"State of Qatar"},
    {"name":"Réunion","alpha_2":"RE","alpha_3":"REU","numeric":"638","official_name":"Réunion"},
    {"name":"Romania","alpha_2":"RO","alpha_3":"ROU","numeric":"642","official_name":"Romania"},
    {"name":"Russian Federation","alpha_2":"RU","alpha_3":"RUS","numeric":"643","official_name":"Russian Federation"},
    ...
]
```

Country details
```bash
curl -D- "http://127.0.0.1:8123/countries/de"
HTTP/1.1 200 OK
date: Thu, 20 Mar 2025 10:17:02 GMT
server: uvicorn
content-length: 971
content-type: application/json

{
  "name":"Germany",
  "alpha_2":"DE",
  "alpha_3":"DEU",
  "numeric":"276",
  "official_name":"Federal Republic of Germany",
  "subdivisions":[
    {"name":"Brandenburg","code":"DE-BB","type":"Land"},
    {"name":"Berlin","code":"DE-BE","type":"Land"},
    {"name":"Baden-Württemberg","code":"DE-BW","type":"Land"},
    {"name":"Bavaria","code":"DE-BY","type":"Land"},
    {"name":"Bremen","code":"DE-HB","type":"Land"},
    {"name":"Hessen","code":"DE-HE","type":"Land"},
    {"name":"Hamburg","code":"DE-HH","type":"Land"},
    {"name":"Mecklenburg-Vorpommern","code":"DE-MV","type":"Land"},
    {"name":"Niedersachsen","code":"DE-NI","type":"Land"},
    {"name":"Nordrhein-Westfalen","code":"DE-NW","type":"Land"},
    {"name":"Rheinland-Pfalz","code":"DE-RP","type":"Land"},
    {"name":"Schleswig-Holstein","code":"DE-SH","type":"Land"},
    {"name":"Saarland","code":"DE-SL","type":"Land"},
    {"name":"Sachsen","code":"DE-SN","type":"Land"},
    {"name":"Sachsen-Anhalt","code":"DE-ST","type":"Land"},
    {"name":"Thüringen","code":"DE-TH","type":"Land"}
  ]
}
```

List subdivisions for specific country
```bash
curl -D- "http://127.0.0.1:8123/countries/de/subdivisions"
HTTP/1.1 200 OK
date: Thu, 20 Mar 2025 10:18:59 GMT
server: uvicorn
content-length: 844
content-type: application/json

[
    {"name":"Brandenburg","code":"DE-BB","type":"Land"},
    {"name":"Berlin","code":"DE-BE","type":"Land"},
    {"name":"Baden-Württemberg","code":"DE-BW","type":"Land"},
    {"name":"Bavaria","code":"DE-BY","type":"Land"},
    {"name":"Bremen","code":"DE-HB","type":"Land"},
    {"name":"Hessen","code":"DE-HE","type":"Land"},
    {"name":"Hamburg","code":"DE-HH","type":"Land"},
    {"name":"Mecklenburg-Vorpommern","code":"DE-MV","type":"Land"},
    {"name":"Niedersachsen","code":"DE-NI","type":"Land"},
    {"name":"Nordrhein-Westfalen","code":"DE-NW","type":"Land"},
    {"name":"Rheinland-Pfalz","code":"DE-RP","type":"Land"},
    {"name":"Schleswig-Holstein","code":"DE-SH","type":"Land"},
    {"name":"Saarland","code":"DE-SL","type":"Land"},
    {"name":"Sachsen","code":"DE-SN","type":"Land"},
    {"name":"Sachsen-Anhalt","code":"DE-ST","type":"Land"},
    {"name":"Thüringen","code":"DE-TH","type":"Land"}
]
```

## Localization
There is build in localization support. To use it you have to add query parameter `lang={code}`, where code - 
the 2 letters code of the language

```bash
curl -D- "http://127.0.0.1:8123/countries/de?lang=de"

HTTP/1.1 200 OK
date: Thu, 20 Mar 2025 10:21:30 GMT
server: uvicorn
content-length: 973
content-type: application/json

{
  "name":"Deutschland",
  "alpha_2":"DE",
  "alpha_3":"DEU",
  "numeric":"276",
  "official_name":"Bundesrepublik Deutschland",
  "subdivisions":[
    {"name":"Brandenburg","code":"DE-BB","type":"Land"},
    {"name":"Berlin","code":"DE-BE","type":"Land"},
    {"name":"Baden-Württemberg","code":"DE-BW","type":"Land"},
    {"name":"Bayern","code":"DE-BY","type":"Land"},
    {"name":"Bremen","code":"DE-HB","type":"Land"},
    {"name":"Hessen","code":"DE-HE","type":"Land"},
    {"name":"Hamburg","code":"DE-HH","type":"Land"},
    {"name":"Mecklenburg-Vorpommern","code":"DE-MV","type":"Land"},
    {"name":"Niedersachsen","code":"DE-NI","type":"Land"},
    {"name":"Nordrhein-Westfalen","code":"DE-NW","type":"Land"},
    {"name":"Rheinland-Pfalz","code":"DE-RP","type":"Land"},
    {"name":"Schleswig-Holstein","code":"DE-SH","type":"Land"},
    {"name":"Saarland","code":"DE-SL","type":"Land"},
    {"name":"Sachsen","code":"DE-SN","type":"Land"},
    {"name":"Sachsen-Anhalt","code":"DE-ST","type":"Land"},
    {"name":"Thüringen","code":"DE-TH","type":"Land"}
  ]
}
```