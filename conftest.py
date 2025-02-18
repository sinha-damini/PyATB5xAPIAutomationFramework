# Reason : To reuse the Create Token and Create Booking.

#create token and create booking Id.

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils



import allure
import pytest


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    # Log the response to check its contents
    print(response.text)  # This will print the full response body
    response_json = response.json()
    token = response_json["token"]
    return token

    verify_http_status_code(response_data=response, expected_data=200)


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_not_null(booking_id)
    return booking_id

