import json
from httpx import Client as httpx

from .ext.utilities.headers import Headers
from.ext.utilities.exceptions import CheckException
from.ext.utilities.objects import *


class Client():
    def __init__(self):
        self.api = "https://api.internal.temp-mail.io/api/v3"

        self.request = httpx().request
        self.headers = Headers().headers

    
    def _make_request(self, method, url, json_data=None):
        response = self.request(method, url, headers=self.headers, json=json_data)
        print(response.status_code)
        if response.status_code != 200:
            error_message = response.json()
            error_message["code"] = response.status_code
            return CheckException(error_message)
        return response
    


    def generate_random_email(self, min_name_length: int = 5, max_name_length: int = 7):
        data = {
            "min_name_length": min_name_length,
            "max_name_length": max_name_length
            }
        
        response = self._make_request("POST", f"{self.api}/email/new", data).json()

        return GenerateEmail(response)
    
    def generate_custom_email(self, name: str, domain: str):
        data = {
            "domain": domain,
            "name": name
            }
        
        response = self._make_request("POST", f"{self.api}/email/new", data).json()

        return GenerateEmail(response)
    
    
    def delete_email(self, email: str, token: str):
        data = {
            "token": token
            }
        
        response = self._make_request("DELETE", f"{self.api}/email/{email}", data).status_code

        return response
    
    
    def get_messages(self, email: str):
        response = self._make_request("GET", f"{self.api}/email/{email}/messages").json()

        return MessageList(response)
    
    
    def get_domains(self):
        response = self._make_request("GET", f"{self.api}/domains").json()

        return DomainList(response)
    
