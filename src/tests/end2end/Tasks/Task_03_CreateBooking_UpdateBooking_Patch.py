import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestE2E_03(object):

    @allure.title("TC03 - Create a Booking > Patch.")
    @allure.description("Verify that a Booking Id is getting created and updated partially.")
    @allure.testcase(url = "https://bugz.atlassian.net/browse/BUG-1", name = "E2E_TC03")
    def test_patch_update_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token

        response = patch_requests(
            url=APIConstants.url_patch_put_delete(booking_id=booking_id),
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking_patch(),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json()["firstname"], "Shikha")
        verify_response_key(response.json()["lastname"], "Srivastava")





#  pytest -s src/tests/end2end/Tasks/Task_03_CreateBooking_UpdateBooking_Patch.py