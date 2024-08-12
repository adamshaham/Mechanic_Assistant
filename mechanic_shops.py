import requests
from geopy.geocoders import Nominatim

def find_repair_shops(api_key, query="repair shop", location=""):
    # Get the latitude and longitude of the specified location
    geolocator = Nominatim(user_agent="repair_shop_locator")
    location_data = geolocator.geocode(location)

    if not location_data:
        print("Location not found.")
        return

    latitude = location_data.latitude
    longitude = location_data.longitude

    # Google Places API endpoint for nearby search
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # Define the parameters
    params = {
        "location": f"{latitude},{longitude}",
        "radius": 5000,  # Search within 5 km radius
        "type": "car_repair",  # Can be modified to find specific types of repair shops
        "keyword": query,
        "key": api_key
    }

    # Make a request to the API
    response = requests.get(url, params=params)
    results = response.json().get('results', [])

    if not results:
        print("No repair shops found in this area.")
        return

    # Print the results with phone numbers
    print(f"Repair shops near {location}:")
    for shop in results:
        name = shop.get('name')
        address = shop.get('vicinity')
        place_id = shop.get('place_id')

        # Make another request to get details like phone number
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            "place_id": place_id,
            "fields": "formatted_phone_number",
            "key": api_key
        }
        details_response = requests.get(details_url, params=details_params)
        details_result = details_response.json().get('result', {})
        phone_number = details_result.get('formatted_phone_number', 'Phone number not available')

        print(f"- {name}, Address: {address}, Phone: {phone_number}")

# Example usage
api_key = "AIzaSyD54qKTI0lCbaoNuOBU1PC__wtvuyKZySQ"  # Replace with your actual Google Places API key
location = "New York, NY"
find_repair_shops(api_key, location=location)
