# **Country Information API Service**

This Country Information API Service is designed to retrieve informations and flag images about any country.

## **Usage :**

1. Navigate to the project directory
2. Run the app using the following command:
    
    ```
    python python/server.py
    ```
    
3. Send a GET request to the following endpoint: where **`<query>`** is the keyword related to the country you want information about.
    
    ```
    http://localhost:105/api/v1/country/<query>
    ```
    
4. The API will return a JSON object with the following information:
    
    ```
   {
        "name": "Australia",
        "alpha-2": "AU",
        "alpha-3": "AUS",
        "country-code": "036",
        "iso_3166-2": "ISO 3166-2:AU",
        "region": "Oceania",
        "sub-region": "Australia and New Zealand",
        "intermediate-region": "",
        "region-code": "009",
        "sub-region-code": "053",
        "intermediate-region-code": ""
    }
    ```
    
5. Send a GET request to the following endpoint:where **`<query>`** is the keyword related to the country you want to get its flag.
    
    ```
    http://localhost:105/api/v1/country/flag/<query>
    ```
    

## **Acknowledgements :**
The data source : https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes
The flags picture : https://countryflagsapi.com 
