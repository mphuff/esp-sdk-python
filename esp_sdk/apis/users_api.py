# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
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


class UsersApi(object):
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

    def create(self, email, first_name, last_name, **kwargs):
        """
        Create a(n) User
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(email, first_name, last_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email: The email of the user (required)
        :param str first_name: The first name of the user (required)
        :param str last_name: The last name of the user (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :param str access_level: The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level
        :param bool disable_daily_emails: Specifies whether the daily emails should be turned off or not
        :param str phone: The phone number of the user
        :param int role_id: The ID of the role of the user. Only a manager can set or modify the role id.
        :param list[int] sub_organization_ids: A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids.
        :param list[int] team_ids: A list of team IDs that the user should have access to. Only a manager can set or modify the team ids.
        :param str time_zone: The time zone of the user. See Time Zones for a list of valid time zones
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(email, first_name, last_name, **kwargs)
        else:
            (data) = self.create_with_http_info(email, first_name, last_name, **kwargs)
            return data

    def create_with_http_info(self, email, first_name, last_name, **kwargs):
        """
        Create a(n) User
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(email, first_name, last_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email: The email of the user (required)
        :param str first_name: The first name of the user (required)
        :param str last_name: The last name of the user (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :param str access_level: The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level
        :param bool disable_daily_emails: Specifies whether the daily emails should be turned off or not
        :param str phone: The phone number of the user
        :param int role_id: The ID of the role of the user. Only a manager can set or modify the role id.
        :param list[int] sub_organization_ids: A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids.
        :param list[int] team_ids: A list of team IDs that the user should have access to. Only a manager can set or modify the team ids.
        :param str time_zone: The time zone of the user. See Time Zones for a list of valid time zones
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'first_name', 'last_name', 'include', 'access_level', 'disable_daily_emails', 'phone', 'role_id', 'sub_organization_ids', 'team_ids', 'time_zone']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params) or (params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `create`")
        # verify the required parameter 'first_name' is set
        if ('first_name' not in params) or (params['first_name'] is None):
            raise ValueError("Missing the required parameter `first_name` when calling `create`")
        # verify the required parameter 'last_name' is set
        if ('last_name' not in params) or (params['last_name'] is None):
            raise ValueError("Missing the required parameter `last_name` when calling `create`")


        collection_formats = {}

        resource_path = '/api/v2/users.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_level' in params:
            form_params.append(('access_level', params['access_level']))
        if 'disable_daily_emails' in params:
            form_params.append(('disable_daily_emails', params['disable_daily_emails']))
        if 'email' in params:
            form_params.append(('email', params['email']))
        if 'first_name' in params:
            form_params.append(('first_name', params['first_name']))
        if 'last_name' in params:
            form_params.append(('last_name', params['last_name']))
        if 'phone' in params:
            form_params.append(('phone', params['phone']))
        if 'role_id' in params:
            form_params.append(('role_id', params['role_id']))
        if 'sub_organization_ids' in params:
            form_params.append(('sub_organization_ids', params['sub_organization_ids']))
            collection_formats['None'] = 'csv'
        if 'team_ids' in params:
            form_params.append(('team_ids', params['team_ids']))
            collection_formats['None'] = 'csv'
        if 'time_zone' in params:
            form_params.append(('time_zone', params['time_zone']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
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

    def delete(self, id, **kwargs):
        """
        Delete a(n) User
        The users current password is required when deleting yourself.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: User ID (required)
        :param str current_password: The user's currently stored password
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_with_http_info(id, **kwargs)
            return data

    def delete_with_http_info(self, id, **kwargs):
        """
        Delete a(n) User
        The users current password is required when deleting yourself.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: User ID (required)
        :param str current_password: The user's currently stored password
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'current_password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")


        collection_formats = {}

        resource_path = '/api/v2/users/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'current_password' in params:
            form_params.append(('current_password', params['current_password']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Meta',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, **kwargs):
        """
        Get a list of Users
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attributes: [id, email] Matching Searchable Attribute: [email]  Sortable Attributes: [email, current_sign_in_at, updated_at, created_at, id] Searchable Associations: [role, organization, sub_organizations, teams] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information.
        :param str page: Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get a list of Users
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attributes: [id, email] Matching Searchable Attribute: [email]  Sortable Attributes: [email, current_sign_in_at, updated_at, created_at, id] Searchable Associations: [role, organization, sub_organizations, teams] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information.
        :param str page: Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'filter', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v2/users.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'filter' in params:
            form_params.append(('filter', params['filter']))
        if 'page' in params:
            form_params.append(('page', params['page']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaginatedCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def show(self, id, **kwargs):
        """
        Show a single User
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: User ID (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_with_http_info(id, **kwargs)
        else:
            (data) = self.show_with_http_info(id, **kwargs)
            return data

    def show_with_http_info(self, id, **kwargs):
        """
        Show a single User
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: User ID (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `show`")


        collection_formats = {}

        resource_path = '/api/v2/users/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
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

    def update(self, id, **kwargs):
        """
        Update a(n) User
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: User ID (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :param str access_level: The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level
        :param bool disable_daily_emails: Specifies whether the daily emails should be turned off or not
        :param str first_name: The first name of the user
        :param str last_name: The last name of the user
        :param str phone: The phone number of the user
        :param int role_id: The ID of the role of the user. Only a manager can set or modify the role id.
        :param list[int] sub_organization_ids: A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids.
        :param list[int] team_ids: A list of team IDs that the user should have access to. Only a manager can set or modify the team ids.
        :param str time_zone: The time zone of the user. See Time Zones for a list of valid time zones
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(id, **kwargs)
        else:
            (data) = self.update_with_http_info(id, **kwargs)
            return data

    def update_with_http_info(self, id, **kwargs):
        """
        Update a(n) User
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: User ID (required)
        :param str include: Related objects that can be included in the response:  organization, sub_organizations, teams, role See Including Objects for more information.
        :param str access_level: The level of access this user has. Team access has access to items belonging only to that team. Sub Organization access has access to items belonging only to all teams under that sub organization. Organization access has access to all sub organizations and teams under that organization. Valid values are organization_level, sub_organization_level, team_level
        :param bool disable_daily_emails: Specifies whether the daily emails should be turned off or not
        :param str first_name: The first name of the user
        :param str last_name: The last name of the user
        :param str phone: The phone number of the user
        :param int role_id: The ID of the role of the user. Only a manager can set or modify the role id.
        :param list[int] sub_organization_ids: A list of sub organization IDs that the user should have access to. Only a manager can set or modify the sub organization ids.
        :param list[int] team_ids: A list of team IDs that the user should have access to. Only a manager can set or modify the team ids.
        :param str time_zone: The time zone of the user. See Time Zones for a list of valid time zones
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include', 'access_level', 'disable_daily_emails', 'first_name', 'last_name', 'phone', 'role_id', 'sub_organization_ids', 'team_ids', 'time_zone']
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
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update`")


        collection_formats = {}

        resource_path = '/api/v2/users/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_level' in params:
            form_params.append(('access_level', params['access_level']))
        if 'disable_daily_emails' in params:
            form_params.append(('disable_daily_emails', params['disable_daily_emails']))
        if 'first_name' in params:
            form_params.append(('first_name', params['first_name']))
        if 'last_name' in params:
            form_params.append(('last_name', params['last_name']))
        if 'phone' in params:
            form_params.append(('phone', params['phone']))
        if 'role_id' in params:
            form_params.append(('role_id', params['role_id']))
        if 'sub_organization_ids' in params:
            form_params.append(('sub_organization_ids', params['sub_organization_ids']))
            collection_formats['None'] = 'csv'
        if 'team_ids' in params:
            form_params.append(('team_ids', params['team_ids']))
            collection_formats['None'] = 'csv'
        if 'time_zone' in params:
            form_params.append(('time_zone', params['time_zone']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

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
