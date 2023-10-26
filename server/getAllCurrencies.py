from static import jsonToDict, dictToJson, navigate

navigate()

countries = jsonToDict("data.json")

currencies = []

unique_currency_names = set()

for country in countries:
    if "currencies" in country.keys():
        currency = country["currencies"][0]
        currency_name = currency["name"]

        if currency_name not in unique_currency_names:
            currencies.append(currency)
            unique_currency_names.add(currency_name)

dictToJson("currencies.json", currencies)
