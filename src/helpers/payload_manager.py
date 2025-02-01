# Payloads

# Create Booking
# Update Booking
# Auth - Token

from dotenv import load_dotenv
import os


def payload_create_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": "Damini",
        "lastname": "Sinha",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-26"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_update_booking_patch():
    payload = {
        "firstname": "Shikha",
        "lastname": "Srivastava"
    }
    return payload

def payload_update_invalid_put():
    payload = {
        "firstname": "Damini",
        "lastname": "Sinha",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-26"
        },
        "additionalneeds": "Breakfast",
    }
    return payload

from dotenv import load_dotenv
import os

def payload_create_token():
    load_dotenv("C:\\Users\\HP\\PycharmProjects\\PyATB5xAPIAutomationFramework\\.env", override=True)

    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }


