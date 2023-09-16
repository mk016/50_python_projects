import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        
        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number.")
            return
        
        country = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        time_zone = timezone.time_zones_for_number(parsed_number)
        
        print("Country:", country)
        print("Service Provider:", service_provider)
        print("Time Zone:", time_zone[0] if time_zone else "Unknown")
    
    except Exception as e:
        print("Error:", str(e))

phone_number = input("Enter a phone number (with country code): ")
get_phone_info(phone_number)
// this project make by mahendra Kumawat
