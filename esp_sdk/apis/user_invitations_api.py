# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserInvitationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def update(self, password, password_confirmation, invitation_token, **kwargs):
        """
        A successful call to this API updates and accepts a User Invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(password, password_confirmation, invitation_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str password: The password for the new user (required)
        :param str password_confirmation: The password confirmation for the new user (required)
        :param str invitation_token: The token generated with the User Invite (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(password, password_confirmation, invitation_token, **kwargs)
        else:
            (data) = self.update_with_http_info(password, password_confirmation, invitation_token, **kwargs)
            return data

    def update_with_http_info(self, password, password_confirmation, invitation_token, **kwargs):
        """
        A successful call to this API updates and accepts a User Invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(password, password_confirmation, invitation_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str password: The password for the new user (required)
        :param str password_confirmation: The password confirmation for the new user (required)
        :param str invitation_token: The token generated with the User Invite (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['password', 'password_confirmation', 'invitation_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `update`")
        # verify the required parameter 'password_confirmation' is set
        if ('password_confirmation' not in params) or (params['password_confirmation'] is None):
            raise ValueError("Missing the required parameter `password_confirmation` when calling `update`")
        # verify the required parameter 'invitation_token' is set
        if ('invitation_token' not in params) or (params['invitation_token'] is None):
            raise ValueError("Missing the required parameter `invitation_token` when calling `update`")


        collection_formats = {}

        resource_path = '/api/v2/users/invitations.json_api'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'password_confirmation' in params:
            form_params.append(('password_confirmation', params['password_confirmation']))
        if 'invitation_token' in params:
            form_params.append(('invitation_token', params['invitation_token']))

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='User',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
