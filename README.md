# **Country Informations API Service**

This Country Information API Service is designed to retrieve informations and flag images about any country.

## **Usage :**

1. Navigate to the project directory
2. Run the app using the following command:

   ```
   python server/server.py
   ```
3. Send a GET request to the following endpoint: where **`<query>`** is the keyword related to the country you want information about.

   ```
   http://localhost:5000/api/v1/country/<query>
   ```
4. The API will return a JSON object with the following information:

   ```
   {
           "name": "Tunisia",
           "topLevelDomain": [
               ".tn"
           ],
           "alpha2Code": "TN",
           "alpha3Code": "TUN",
           "callingCodes": [
               "216"
           ],
           "capital": "Tunis",
           "altSpellings": [
               "TN",
               "Republic of Tunisia",
               "al-Jumhūriyyah at-Tūnisiyyah"
           ],
           "subregion": "Northern Africa",
           "region": "Africa",
           "population": 11818618,
           "latlng": [
               34.0,
               9.0
           ],
           "demonym": "Tunisian",
           "area": 163610.0,
           "gini": 32.8,
           "timezones": [
               "UTC+01:00"
           ],
           "borders": [
               "DZA",
               "LBY"
           ],
           "nativeName": "تونس",
           "numericCode": "788",
           "currencies": [
               {
                   "code": "TND",
                   "name": "Tunisian dinar",
                   "symbol": "د.ت"
               }
           ],
           "languages": [
               {
                   "iso639_1": "ar",
                   "iso639_2": "ara",
                   "name": "Arabic",
                   "nativeName": "العربية"
               }
           ],
           "translations": {
               "br": "Tunizia",
               "pt": "Tunísia",
               "nl": "Tunesië",
               "hr": "Tunis",
               "fa": "تونس",
               "de": "Tunesien",
               "es": "Túnez",
               "fr": "Tunisie",
               "ja": "チュニジア",
               "it": "Tunisia",
               "hu": "Tunézia"
           },
           "regionalBlocs": [
               {
                   "acronym": "AU",
                   "name": "African Union",
                   "otherNames": [
                       "الاتحاد الأفريقي",
                       "Union africaine",
                       "União Africana",
                       "Unión Africana",
                       "Umoja wa Afrika"
                   ]
               },
               {
                   "acronym": "AL",
                   "name": "Arab League",
                   "otherNames": [
                       "جامعة الدول العربية",
                       "Jāmiʻat ad-Duwal al-ʻArabīyah",
                       "League of Arab States"
                   ]
               }
           ],
           "cioc": "TUN",
           "independent": true
       }
   ```
5. Send a GET request to the following endpoint:where **`<query>`** is the keyword related to the country you want to get its flag.

   ```
   http://localhost:5000/api/v1/country/flag/<query>
   ```

## **Acknowledgements :**

Data source : 
- https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes
- https://restcountries.com

Flags picture : 
- https://countryflagsapi.com
