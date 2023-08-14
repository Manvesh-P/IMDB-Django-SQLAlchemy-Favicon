# # import requests


# # res = requests
# # from keycloak import KeycloakOpenID
# # import keycloak
# from keycloak.keycloak_openid import KeycloakOpenID


# # keycloak.Client.

# KEYCLOAK_URL = 'http://127.0.0.1:8080/'
# KEYCLOAK_CLIENT_ID = 'manvesh'
# KEYCLOAK_REALM = 'myrealm'

# keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_URL,
#                                 client_id=KEYCLOAK_CLIENT_ID,
#                                 realm_name=KEYCLOAK_REALM,
#                                 client_secret_key="secret",
#                                 verify=True)
# print(keycloak_openid)
# # print(keycloak_openid.introspect)
# print(keycloak_openid.introspect('eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqQWJ1QXhOS194STRmUXFscGxQdEg3dWU3cjlaT1E1SXVISkViX3IzbDZNIn0.eyJleHAiOjE2OTA5MjM4ODQsImlhdCI6MTY5MDkyMzU4NCwiYXV0aF90aW1lIjoxNjkwOTIzNTgzLCJqdGkiOiJmM2M2ODQ0ZC1iZTVjLTRjMTYtYjk3Yy1iNWJkMTEwNDRhZDkiLCJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjgwODAvcmVhbG1zL215cmVhbG0iLCJzdWIiOiIzYTlhMmE5Zi1iMGU5LTQwMDYtYTNhMy1iZTBhYTI2NmFkYjgiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJtYW52ZXNoIiwic2Vzc2lvbl9zdGF0ZSI6IjJkYjhkNzBkLWIwOWItNDc2ZS1iM2QwLWM0YTdlYmNjNzJhNCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovLzEyNy4wLjAuMTo4MDAwLyJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsibWFudmVzaCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsInNpZCI6IjJkYjhkNzBkLWIwOWItNDc2ZS1iM2QwLWM0YTdlYmNjNzJhNCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoibWFudmVzaCB0ZmFpIiwicHJlZmVycmVkX3VzZXJuYW1lIjoibXl1c2VyIiwiZ2l2ZW5fbmFtZSI6Im1hbnZlc2giLCJmYW1pbHlfbmFtZSI6InRmYWkiLCJlbWFpbCI6Im5wZXl5YWxhQHRlY2hmb3JjZS5haSJ9.fdjXXIznQJQ76-OHhsh83EMxR2rJ_7XCfgZEiOk20syqMGWEifmDzsHJGtIfNoeuIdkDnRjXLD4j0Gpn-Vn_CqbtO9JGJ8lUDK1m8kVREwxn7--sfwIMqFLrRWeTAda49RmrhgK0lmLke4ySpZXfawxGKpOSoLeJfbABiAtUix8w9ak8bSatQSTO5bokjqyAKBl1RgbG4PJ-Yb6wJ3JhpaCEQwCa49nZGfuO96Gu1xA5GJAq36TwEfh1B6hNYBiO_wgT9rS-w90-H9mgAc9sUPhHLMHvKl0BGI2U2-RkuJXZ1lS6Li0jv5HvvpUW90LERwZGOIIp6uPJ7CV9n5oRTw'))


# def fence(_fun):
#     def wrapper(*args, **kwargs):
#         print('+' * 10)
#         res = _fun()
#         print(res)
#         print('+' * 10)

#         return
#     return wrapper


# @fence
# def _info():
#     return 'Entered into "_info" function'

# # print(_info())
# _info()

# def test_fun():
    # yield redirect()

import requests


# _url = 'http://127.0.0.1:8080/realms/myrealm/protocol/openid-connect/login-status-iframe.html'
_url = 'http://127.0.0.1:8080/realms/myrealm/protocol/openid-connect/auth?client_id=manvesh&response_type=code&redirect_uri=http://127.0.0.1:8000/api/IMDBApp/home/view/'
# _url = 'http://127.0.0.1:8080/realms/myrealm/protocol/openid-connect/ext/ciba/auth/'
res = requests.get(url=_url)
# res = requests.post(url=_url, 
#                     # json={'client_id': 'manvesh'}, 
#                     data={'client_id': 'manvesh'}
#                     )

print(res)
# print(res.json())
print(res.text)
print(res.status_code)
