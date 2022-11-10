import os
import json
import requests

API_NAME = "cbsdGrantsStateChanges"
ANALYTICS_API_URL = "add this based on release and envrionment"
IAM_URL_BASE = "add this based on release and envrionment"

def pseudo_auth():

    try:
        email = "you email address for the account"
        password = "your password"
        body = {"email": email, "password": password}
        signin_url = IAM_URL_BASE + "signin"
        response = requests.post(url=signin_url, data=json.dumps(body))
        r = response.json()
        auth = "Bearer " + r["jwtToken"]
        return auth
    except Exception as e:
        EXCEPTION_MESSAGE = "Authentication failed"
        raise

    if response.status_code != 200:
        EXCEPTION_MESSAGE = "Authentication failed"
        raise

    r = response.json()
    if "jwtToken" in r:
        return "Bearer " + r["jwtToken"]

def get_api_response(api_name, params_payload={}, body_payload={}):
    try:
        # get authentication
        auth = pseudo_auth()
        headers = {"Content-Type": "application-json", "Authorization": auth}
        url = ANALYTICS_API_URL + api_name
        # call api and return response
        response = requests.post(
            url, data=json.dumps(body_payload), headers=headers, params=params_payload
        )

        return response
    except (Exception) as e:
        print(e)
        raise


def fetch_api_results():
    # customized your own query paras with modifying cbsdId,startTime and endTime
    QUERY_PARAMS = {
        "cbsdId": "XXXX",
        "startTime": "2022-11-01T01:01:01Z",
        "endTime": "2022-11-04T01:01:01Z"
        }
    try:
        response = get_api_response(API_NAME, QUERY_PARAMS, {}).json()
        grants_list = response["grantsStateChangesList"]
        for grant in grants_list:
            print(grant)
            pass
        # this is just example, you can fetch other fields
    except Exception as e:
        print(e)