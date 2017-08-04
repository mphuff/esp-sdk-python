# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class CloudTrailEvent(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, event_id=None, event_name=None, event_time=None, ip_address=None, user_agent=None, username=None, errors=None):
        """
        CloudTrailEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'event_id': 'int',
            'event_name': 'str',
            'event_time': 'datetime',
            'ip_address': 'str',
            'user_agent': 'str',
            'username': 'str',
            'errors': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'event_id': 'event_id',
            'event_name': 'event_name',
            'event_time': 'event_time',
            'ip_address': 'ip_address',
            'user_agent': 'user_agent',
            'username': 'username',
            'errors': 'errors'
        }

        self._id = id
        self._event_id = event_id
        self._event_name = event_name
        self._event_time = event_time
        self._ip_address = ip_address
        self._user_agent = user_agent
        self._username = username
        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this CloudTrailEvent.
        Unique ID

        :return: The id of this CloudTrailEvent.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudTrailEvent.
        Unique ID

        :param id: The id of this CloudTrailEvent.
        :type: int
        """

        self._id = id

    @property
    def event_id(self):
        """
        Gets the event_id of this CloudTrailEvent.
        GUID generated by CloudTrail to uniquely identify each event

        :return: The event_id of this CloudTrailEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this CloudTrailEvent.
        GUID generated by CloudTrail to uniquely identify each event

        :param event_id: The event_id of this CloudTrailEvent.
        :type: int
        """

        self._event_id = event_id

    @property
    def event_name(self):
        """
        Gets the event_name of this CloudTrailEvent.
        The requested action, which is one of the actions listed in the API Reference for the service

        :return: The event_name of this CloudTrailEvent.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this CloudTrailEvent.
        The requested action, which is one of the actions listed in the API Reference for the service

        :param event_name: The event_name of this CloudTrailEvent.
        :type: str
        """

        self._event_name = event_name

    @property
    def event_time(self):
        """
        Gets the event_time of this CloudTrailEvent.
        ISO 8601 timestamp when the cloud trail event occurred

        :return: The event_time of this CloudTrailEvent.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this CloudTrailEvent.
        ISO 8601 timestamp when the cloud trail event occurred

        :param event_time: The event_time of this CloudTrailEvent.
        :type: datetime
        """

        self._event_time = event_time

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CloudTrailEvent.
        The apparent IP address that the request was made from for the given event

        :return: The ip_address of this CloudTrailEvent.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CloudTrailEvent.
        The apparent IP address that the request was made from for the given event

        :param ip_address: The ip_address of this CloudTrailEvent.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def user_agent(self):
        """
        Gets the user_agent of this CloudTrailEvent.
        The agent through which the request was made, such as the AWS Management Console or an AWS SDK

        :return: The user_agent of this CloudTrailEvent.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this CloudTrailEvent.
        The agent through which the request was made, such as the AWS Management Console or an AWS SDK

        :param user_agent: The user_agent of this CloudTrailEvent.
        :type: str
        """

        self._user_agent = user_agent

    @property
    def username(self):
        """
        Gets the username of this CloudTrailEvent.
        The user name associated with the cloud trail event

        :return: The username of this CloudTrailEvent.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CloudTrailEvent.
        The user name associated with the cloud trail event

        :param username: The username of this CloudTrailEvent.
        :type: str
        """

        self._username = username

    @property
    def errors(self):
        """
        Gets the errors of this CloudTrailEvent.
        Array of error messages if the request failed

        :return: The errors of this CloudTrailEvent.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this CloudTrailEvent.
        Array of error messages if the request failed

        :param errors: The errors of this CloudTrailEvent.
        :type: list[str]
        """

        self._errors = errors

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CloudTrailEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
