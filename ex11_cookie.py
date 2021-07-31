import requests

class TestCookie:

    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)

        assert response.status_code == 200, "Wrong response code"
        response_cookie = response.cookies
        print(response_cookie)
        assert "HomeWork" in response_cookie, "There is no Cookie HomeWork"
        expected_value = "hw_value"
        actual_value = response_cookie["HomeWork"]
        print(actual_value)
        assert actual_value == expected_value, f"There is \"{actual_value}\" instead of \"{expected_value}\""

