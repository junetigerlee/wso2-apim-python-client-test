from __future__ import print_function
import time
import wso2_apim_tokenclient
from wso2_apim_tokenclient.rest import ApiException
from pprint import pprint

wso2_apim_tokenclient.configuration.host = 'https://localhost:9443/oauth2'
wso2_apim_tokenclient.configuration.verify_ssl =False

# Configure HTTP basic authorization: basicAuth
# consumer-key
wso2_apim_tokenclient.configuration.username = 'm6JOCjvy37tYJVnZwc45YBwXI8Ma'
# consumer-secret
wso2_apim_tokenclient.configuration.password = 'X1wHOdsDkG6SYnJ_PufkVs1ioica'
# create an instance of the API class
api_instance = wso2_apim_tokenclient.TokenApi()
grant_type = 'password' # str |
username = 'admin' # str |  (optional)
password = 'admin' # str |  (optional)
# refresh_token = 'refresh_token_example' # str |  (optional)
scope = 'apim:tier_manage' # str |  (optional)

try:
    # generate access tokens and authorize them
    api_response = api_instance.token_post(grant_type, username=username, password=password, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->token_post: %s\n" % e)

# refresh_token
grant_type = 'refresh_token' # str |
refresh_token = 'a61dc0d8-31b8-34fb-a4e0-ee95707c4b4b' # str |  (optional)
try:
    # generate access tokens and authorize them
    api_response = api_instance.token_post(grant_type, refresh_token=refresh_token, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->token_post: %s\n" % e)


# refresh_token
grant_type = 'refresh_token' # str |
refresh_token = 'a61dc0d8-31b8-34fb-a4e0-ee95707c4b4b' # str |  (optional)
try:
    # generate access tokens and authorize them
    api_response = api_instance.token_post(grant_type, refresh_token=refresh_token, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->token_post: %s\n" % e)


# # client_credentials
# grant_type = 'client_credentials' # str |
#
# try:
#     # generate access tokens and authorize them
#     api_response = api_instance.token_post(grant_type)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling TokenApi->token_post: %s\n" % e)

