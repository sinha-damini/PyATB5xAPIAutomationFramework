import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestE2E_06(object):

    @allure.title("TC06 - Update without Token.")
    @allure.description("Verify that getting 403 response while trying to update without token.")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2E_TC06")
    def test_update_booking_with_id_token(self, get_booking_id):
        print(get_booking_id)
        booking_id = get_booking_id
        response = put_requests(
            url=APIConstants.url_patch_put_delete(booking_id=booking_id),
            headers=Utils().common_header_put_delete_patch_cookie(token=None),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        print("Tryinng to Update without Token.")
        verify_http_status_code(response_data=response, expected_data=403)
        print("403 Forbidden – Authentication is valid, but the user does not have permission.")


# pytest -s src/tests/end2end/Tasks/Task_06_Update_Without_Token.py