from httpx import Client as httpx

from .ext.utilities.headers import Headers
from .ext.utilities.exceptions import CheckException
from .ext.utilities.objects import *


class Client:
    """
    The main client for interacting with the API.
    """

    def __init__(self):
        self.api: str = "https://api.internal.temp-mail.io/api/v3"

        self.request = httpx().request
        self.headers = Headers().headers



    def _make_request(self, method: str, url: str, json_data=None):
        """
        Makes an HTTP request to the specified URL.

        Args:
            method (str): The HTTP method (GET, POST, DELETE, etc.).
            url (str): The URL to make the request to.
            json_data (dict, optional): JSON data to send with the request.

        Returns:
            dict or CheckException: The response from the HTTP request.

        Raises:
            CheckException: If the response status code is not 200.
        """

        response = self.request(method, url, headers=self.headers, json=json_data)

        if response.status_code != 200:
            error_message = response.json()
            error_message["code"] = response.status_code
            return CheckException(error_message)

        return response



    def generate_random_email(self, min_name_length: int = 5, max_name_length: int = 7) -> GenerateEmail:
        """
        Generates a random email address.

        Args:
            min_name_length (int, optional): The minimum length of the email name.
            max_name_length (int, optional): The maximum length of the email name.

        Returns:
            GenerateEmail: The generated email address and token.
        """

        data = {
            "min_name_length": min_name_length,
            "max_name_length": max_name_length
        }

        response = self._make_request("POST", f"{self.api}/email/new", data).json()

        return GenerateEmail(response)



    def generate_custom_email(self, name: str, domain: str) -> GenerateEmail:
        """
        Generates a custom email address.

        Args:
            name (str): The name for the email address.
            domain (str): The domain for the email address.

        Returns:
            GenerateEmail: The generated email address and token.
        """

        data = {
            "domain": domain,
            "name": name
        }

        response = self._make_request("POST", f"{self.api}/email/new", data).json()

        return GenerateEmail(response)



    def delete_email(self, email: str, token: str) -> int:
        """
        Deletes an email address.

        Args:
            email (str): The email address to delete.
            token (str): The token for the email address.

        Returns:
            int: The HTTP status code indicating the success of the operation.
        """

        data = {
            "token": token
        }

        response = self._make_request("DELETE", f"{self.api}/email/{email}", data).status_code

        return response



    def get_messages(self, email: str) -> MessageList:
        """
        Retrieves messages for an email address.

        Args:
            email (str): The email address to retrieve messages for.

        Returns:
            MessageList: The list of messages for the email address.
        """

        response = self._make_request("GET", f"{self.api}/email/{email}/messages").json()

        return MessageList(response)



    def get_domains(self) -> DomainList:
        """
        Retrieves a list of available domains.

        Returns:
            DomainList: The list of available domains.
        """

        response = self._make_request("GET", f"{self.api}/domains").json()

        return DomainList(response)


