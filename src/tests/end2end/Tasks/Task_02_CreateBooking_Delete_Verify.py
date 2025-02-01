import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class TestE2E_02(object):

    @allure.title("TC02 - Create a Booking > Delete it > Verify the Deletion.")
    @allure.description("Verify that a Booking Id is getting created and deleted.")
    @allure.testcase(url = "https://bugz.atlassian.net/browse/BUG-1", name = "E2E_TC02")

    def test_delete_booking_id(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(delete_url)

        response = delete_requests(
            url = delete_url,
            headers = Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)
        print("Created Booking Id: "+ str(booking_id) + " is deleted.")

        print("Verify that it got deleted.")

        response_get = get_request(
            url=APIConstants.get_booking_url(booking_id=booking_id),
            auth= None,
            in_json=False)

        assert response_get.status_code == 404

#  pytest -s src/tests/end2end/Tasks/Task_02_CreateBooking_Delete_Verify.py