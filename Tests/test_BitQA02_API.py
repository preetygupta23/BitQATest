import json

import requests


def test_patch_api():
    url = "https://api.restful-api.dev/"
    headers = {"Content-Type": "application/json"}

    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

    response = requests.patch(url, headers=headers, json=payload)  # Check the response

    # Assertions to check the response
    assert response.status_code == 200, f"PATCH request was successful."
    assert "name" in response.json(), "The response does contain the name field."


