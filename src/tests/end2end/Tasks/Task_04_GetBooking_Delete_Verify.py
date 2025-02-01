import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class TestE2E_04(object):

    @allure.title("TC04 - Get Booking and Delete it.")
    @allure.description("Verify that an existing booking Id is getting deleted.")
    @allure.testcase(url = "https://bugz.atlassian.net/browse/BUG-1", name = "E2E_TC04")

    def test_get_delete_booking_id(self, create_token):
        print(create_token)
        token = create_token

        response_get = get_request(
            url = APIConstants().url_create_booking(),
            auth=None,
            in_json=False
        )



        booking_id = response_get.json()[2]["bookingid"]
        print(booking_id)

        print("Deleting this Booking Id: ", booking_id)

        response_delete = delete_requests(
            url=APIConstants.url_patch_put_delete(booking_id=booking_id),
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response_delete, expected_data=201)
        verify_response_delete(response=response_delete.text)
        print("Created Booking Id: " + str(booking_id) + " is deleted.")

        print("Verifying that it got deleted.")

        response_get = get_request(
            url=APIConstants.get_booking_url(booking_id=booking_id),
            auth=None,
            in_json=False)

        assert response_get.status_code == 404
        print("Assertion passed -> Id successfully Deleted.")

#  pytest -s src/tests/end2end/Tasks/Task_04_GetBooking_Delete_Verify.py