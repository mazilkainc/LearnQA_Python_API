import requests

class TestHeader:

    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)

        assert response.status_code == 200, "Wrong response code"
        response_header = response.headers
        print(response_header)
        assert "x-secret-homework-header" in response_header, "There is no \"x-secret-homework-header\" in response"
        expected_value = "Some secret value"
        actual_value = response_header["x-secret-homework-header"]
        assert actual_value == expected_value, f"There is {actual_value} instead of {expected_value}"

