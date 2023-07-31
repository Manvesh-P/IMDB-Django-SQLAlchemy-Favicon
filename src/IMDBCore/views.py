from django.shortcuts import (render, 
                              redirect)
from django.contrib.auth import (authenticate, 
                                 login, 
                                 logout)
from django.http import JsonResponse
from IMDBCore.models import (User, 
                             Organisation)
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from session_maker import SessionManager
from datetime import time
from sqlalchemy import and_


session = SessionManager().get_session()
# Create your views here.
def token_is_valid(access_token):
    import keycloak
    from keycloak import KeycloakOpenID
    # KEYCLOAK_URL = os.environ.get('KEYCLOAK_URL') or config('KEYCLOAK_URL')
    KEYCLOAK_URL = 'http://127.0.0.1:8080/'
    # KEYCLOAK_REALM = os.environ.get('KEYCLOAK_REALM') or config('KEYCLOAK_REALM')
    KEYCLOAK_REALM = 'myrealm'
    # KEYCLOAK_CLIENT_ID = os.environ.get('KEYCLOAK_CLIENT_ID') or config('KEYCLOAK_CLIENT_ID')
    KEYCLOAK_CLIENT_ID = 'manvesh'
    keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_URL,
                                     client_id=KEYCLOAK_CLIENT_ID,
                                     realm_name=KEYCLOAK_REALM,
                                     client_secret_key="secret",
                                     verify=True
                                    )
    try:
        userinfo = keycloak_openid.userinfo(access_token)
        print(userinfo,'userinfo----------------')
        a=userinfo.get("preferred_username")
        print(a)
        return a
    except Exception as e:
        print('eeeeeee')
        print(str(e))


def authenticate_access(fn):
    def wrapfn(*args, **kwargs):
        rv = ''
        # access_token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJtaFVFNDEybUQ0Z0JUMTdhMXJzVFpRRkF5enVRSHpSMWhDaVV5M3VBU3pRIn0.eyJleHAiOjE1OTg4NTAzNTMsImlhdCI6MTU5ODg0OTc1MywianRpIjoiMTAxNTY2MTQtZmVjZC00YWM3LWJmYTEtNjU3ODYzNWJkMzc5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL3NhbXBsZSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2ODJkZjI0ZC1mOTE3LTRiMGMtYWQ0ZS02ZTFhZGM2OGFmMzMiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3ZWJhcHAiLCJzZXNzaW9uX3N0YXRlIjoiZGQ5MWU4YmQtODhlNS00NzdkLWI2ZmMtNWU0OTBmYjdmMjMxIiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoid2VidXNlciJ9.T62Fose_AVo0bTfT78LjvpgNb6kniswY7XHc11fRhU6kiDhgmRjzu8TNKaLYq-f6F5qQa4uhOpKoPU80ulHb_Lpc8FoJZyDoErgww1W4n4TD-3qgesQOAiE-Fw1MF_diDktXsNwQQhK7rjc7VmHAJC8hP6Y1WKFMmqDk7hjoUS02i59lVX2CexxAXBfrHoGHSTBFPy-kzD7CjPZq40-vG1hyAm5muSEhjznEzauKE2gB-a9GU_ZE1isbcUUAPPp5cxuWEEYRW1WC3E42heqqof3bcXXWd90ZGRY2sTbEFIuZRaJ6Qq8yGYijt_fXc6nuVVdIX8ceOnvkzyNp2N3oBA"
        access_token=args[1].META["HTTP_AUTHORIZATION"]
        access_token=access_token.replace("Bearer ","")
        if token_is_valid(access_token):
            rv = fn(*args, **kwargs)
        else:
            return Response("unauthorized user", status=status.HTTP_400_BAD_REQUEST)
            rv="Anauthorized user"
        return rv
    return wrapfn
# @login_required
def main_view(request):
    return render(request, 'index.html', {'extra': None})

def login_view(request):
    return render(request, 'index.html', {'page': 'login', 'extra': None})

def logout_view(request):
    logout(request)
    # logger.info('Called Logout')
    return redirect('/login')

# Create your views here.

# class TestTaskApi(APIView):
#     def get(self, request):
#         for v in range(0,1):
#             print_msg.delay("Hello world") #calling the task on the task engine
#         return Response({"status": "Task started"})

class OrganisationList(APIView):
    def get(self, request):
        # engine = sqlalchemy.create_engine(SQLALCHEMY_HOST,poolclass=sqlalchemy.pool.NullPool)
        # session = sqlalchemy.orm.sessionmaker(bind=engine, autoflush=False)()
        session_obj = session()
        try:
            org_list = session.query(Organisation).all()
            org_dict_li = []
            for data in org_list:
                org_info = {'organisationId':data.org_id, 'organisationName':data.org_name}
                org_dict_li.append(org_info)
        except:
            session_obj.rollback()
            raise
        finally:
            session_obj.close()
            # engine.dispose()
        return JsonResponse(org_dict_li, safe=False)

class SubmitApi(APIView):
    def post(self, request):
        #print('hi sabdjkan')
        usr_name = request.data["username"]
        usr_pwd = request.data["password"]

        #role=request.data['role']

        # engine = sqlalchemy.create_engine(SQLALCHEMY_HOST,poolclass=sqlalchemy.pool.NullPool)
        # session = sqlalchemy.orm.sessionmaker(bind=engine, autoflush=False)()
        session_obj = session()
        try:
            all_db = session_obj.query(User).all()
        except:
            session_obj.rollback()
            raise
        finally:
            session_obj.close()
            # engine.dispose()

        pwd = False
        usr = False
        unm = ''
        for c in all_db:
            if c.user_username == usr_name:
                usr =True
                unm = c.user_username
                if c.user_password == usr_pwd:
                    pwd = True
                    print(c.user_username , ' your role is "' , c.user_role , '"')
                    role_user=c.user_role

                    approver_count = c.user_approver_count
                    if approver_count == None:
                        approver_count = "SINGLE"

                    return Response({
                        "role":role_user.lower(),
                        "user": c.user_username,
                        "userUId": c.user_uid,
                        "orgId": c.org_id,
                        "approvers": approver_count
                        })

        if usr == True and pwd == False:
            print(unm , 'pls check your pwd')
            error_message = unm + ' pls check your pwd'
            return Response({'error': error_message},status=status.HTTP_409_CONFLICT)
        if usr==False:
            print('user not valid')
            error_message = 'user not valid'
            return Response({"error": error_message},status=status.HTTP_406_NOT_ACCEPTABLE)


class SignupApi(APIView):
    def post(self, request):
        usr_name = request.data["username"]
        usr_pwd = request.data['password']
        usr_role = request.data['role']
        usr_org_id = request.data["orgId"]

        # engine = sqlalchemy.create_engine(SQLALCHEMY_HOST,poolclass=sqlalchemy.pool.NullPool)
        # session = sqlalchemy.orm.sessionmaker(bind=engine, autoflush=False)()
        session_obj = session()
        try:
            temp_data = session_obj.query(User).filter(
                and_(
                    User.user_username == usr_name,
                    User.org_id == usr_org_id
                )
            ).all()
            last_user = session_obj.query(User).filter(
                User.org_id == usr_org_id
            ).order_by(
                User.user_id.desc()
            ).first()
            if temp_data:
                message = "user already exist"
                print(message)
                return Response({"status":message}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                if last_user == None:
                    user_id = 1
                else:
                    user_id = last_user.user_id + 1
                user = User(
                    org_id = usr_org_id,
                    user_id = user_id,
                    user_created_date = time.strftime("%Y-%m-%d %H:%M:%S GMT", time.gmtime()),
                    user_username = usr_name,
                    user_password = usr_pwd,
                    user_role = usr_role,
                )
                session_obj.add(user)
                session_obj.commit()
                error_message = 'user added successfully'
                print(error_message)
                return Response({"status": error_message},status=status.HTTP_201_CREATED)
        except:
            session_obj.rollback()
            raise
        finally:
            session_obj.close()
            # engine.dispose()


class LogoutApi(APIView):
    def get(self, request):
        logout(request)
        return Response({'statusText': 'success'})
