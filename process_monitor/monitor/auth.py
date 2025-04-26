from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class SimpleAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith("Token "):
            api_key = auth_header.split("Token ")[1]
            if api_key == "your-api-key": 
                return (None, None)
        raise AuthenticationFailed('Invalid API key')
