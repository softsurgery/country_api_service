# **Country Information API Service**

This Country Information API Service is designed to retrieve informations and flag images about any country.

## **Usage :**

1. Navigate to the project directory
2. Run the app using the following command:
    
    ```
    python app.py
    ```
    
3. Send a GET request to the following endpoint:where **`<country_code>`** is the name of the country you want information about.
    
    ```
    bashCopy code
    http://localhost:105/api/v1/country/country_code
    ```
    
4. The API will return a JSON object with the following information:
    
    ```
    {
            "name": "Afghanistan",
            "alpha-2": "AF",
            "alpha-3": "AFG",
            "country-code": "004",
            "iso_3166-2": "ISO 3166-2:AF",
            "region": "Asia",
            "sub-region": "Southern Asia",
            "intermediate-region": "",
            "region-code": "142",
            "sub-region-code": "034",
            "intermediate-region-code": ""
     }
    ```
    
5. Send a GET request to the following endpoint:where **`<country_code>`** is the name of the country you want to get its flag.
    
    ```
    http://localhost:105/api/v1/country/flag/country_code
    ```
    

## **Acknowledgements :**
