import requests
import json

class Client:
    """
    Client class to query to the Powererp backend
    """

    def __init__(self, url, token):
        """
        Class constructor
        :param url: Base URL of the backend
        :type url: str
        :param token:
        :type token:
        """

        self.backend_url = url
        self.token = token

    def method(self, model, identifier, method_name):
        """
        Calls a method of model

        :param model: Model
        :type model: str
        :param identifier: Id of the element
        :type model: str,int
        :param method_name: Method of the mode
        :type method_name: str
        :return: Result
        :rtype: dict
        """

        built_url = "{}/{}".format(self.backend_url, model, str(identifier), method_name)
        headers = {"Authorization": "token {}".format(self.token)}
        response = requests.get(built_url, headers=headers)
        print response
        return json.loads(response.content)
