"""This module corresponds to functionality documented
at https://blockchain.info/api/create_wallet

"""

from . import util
import json


def create_wallet(password, api_code, service_url, priv=None, label=None, email=None):
        params = {'password': password, 'api_code': api_code}
        if priv is not None:
            params['priv'] = priv
        if label is not None:
            params['label'] = label
        if email is not None:
            params['email'] = email
        
        response = util.call_api("api/v2/create", params, base_url=service_url)
        json_response = json.loads(response)
        return CreateWalletResponse(json_response['guid'],
                                    json_response['address'],
                                    json_response['label'])


class CreateWalletResponse:
    
    def __init__(self, identifier, address, label):
        self.identifier = identifier
        self.address = address
        self.label = label
