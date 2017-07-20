from __future__ import print_function
import time
import wso2_apim_storeclient
from wso2_apim_storeclient.rest import ApiException
from pprint import pprint

wso2_apim_storeclient.configuration.host = 'https://localhost:9443/api/am/store/v0.11'
wso2_apim_storeclient.configuration.verify_ssl =False

# create an instance of the API class
api_instance = wso2_apim_storeclient.APICollectionApi()
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
x_wso2_tenant = '' # str | For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from.  (optional)
query = '' # str | **Search condition**.  You can search in attributes by using an **\"<attribute>:\"** modifier.  Eg. \"provider:wso2\" will match an API if the provider of the API is exactly \"wso2\".  Additionally you can use wildcards.  Eg. \"provider:wso2*\" will match an API if the provider of the API starts with \"wso2\".  Supported attribute modifiers are [**version, context, status, description, subcontext, doc, provider, tag**]  If no advanced attribute modifier has been specified, search will match the given query string against API Name.  (optional)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try:
    # Retrieve/Search APIs
    api_response = api_instance.apis_get(limit=limit, offset=offset, x_wso2_tenant=x_wso2_tenant, query=query, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APICollectionApi->apis_get: %s\n" % e)