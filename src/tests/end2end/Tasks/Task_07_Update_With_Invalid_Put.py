import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestE2E_07(object):

    @allure.title("TC07 - Update with Invalid Payload")
    @allure.description("Verify that getting error while trying to update with invalid payload.")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2E_TC07")
    def test_update_booking_with_id_token(self, get_booking_id):
        print(get_booking_id)
        booking_id = get_booking_id
        response = put_requests(
            url=APIConstants.url_patch_put_delete(booking_id=booking_id),
            headers=Utils().common_header_put_delete_patch_cookie(token=None),
            payload=payload_update_invalid_put(),
            auth=None,
            in_json=False
        )
        print("Trying to Update with Invalid Put -> Should get some error.")
        verify_http_status_code(response_data=response, expected_data=403)

        verify_response_key(response.json()["firstname"], "Damini")
        verify_response_key(response.json()["lastname"], "Sinha")
        verify_response_key(response.json()["bookingdates"]["checkin"], "2025-01-01")
        verify_response_key(response.json()["bookingdates"]["checkout"], "2025-01-26")


# pytest -s src/tests/end2end/Tasks/Task_07_Update_With_Invalid_Put.py