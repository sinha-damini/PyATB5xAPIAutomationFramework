import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestE2E_05(object):

    @allure.title("TC05 - Delete a Booking and trying to Update.")
    @allure.description("Verify that a booking is deleted and trying to update after this.")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2E_TC05")

    def test_delete_booking_id(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token

        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(
            url= delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )

        print("Verify that it got deleted.")
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)
        print("Created Booking Id: "+ str(booking_id) + " is deleted.")

        print("Trying to update the deleted Id.")



    def test_update_deleted_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token

        response = put_requests(
            url=APIConstants.url_patch_put_delete(booking_id=booking_id),
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=405)

        print("405 Method Not Allowed – The HTTP method (GET, POST, etc.) is not supported.")

# pytest -s src/tests/end2end/Tasks/Task_05_Delete_Update.py