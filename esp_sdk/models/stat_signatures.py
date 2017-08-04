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


class StatSignatures(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, new_1h_pass=None, new_1d_pass=None, new_1w_pass=None, old_pass=None, new_1h_fail=None, new_1d_fail=None, new_1w_fail=None, old_fail=None, new_1h_warn=None, new_1d_warn=None, new_1w_warn=None, old_warn=None, new_1h_error=None, new_1d_error=None, new_1w_error=None, old_error=None, suppressed_pass=None, suppressed_fail=None, suppressed_warn=None, suppressed_error=None, new_1h_info=None, new_1d_info=None, new_1w_info=None, old_info=None, suppressed_info=None, signature=None, signature_id=None, stat=None, stat_id=None, errors=None):
        """
        StatSignatures - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'new_1h_pass': 'int',
            'new_1d_pass': 'int',
            'new_1w_pass': 'int',
            'old_pass': 'int',
            'new_1h_fail': 'int',
            'new_1d_fail': 'int',
            'new_1w_fail': 'int',
            'old_fail': 'int',
            'new_1h_warn': 'int',
            'new_1d_warn': 'int',
            'new_1w_warn': 'int',
            'old_warn': 'int',
            'new_1h_error': 'int',
            'new_1d_error': 'int',
            'new_1w_error': 'int',
            'old_error': 'int',
            'suppressed_pass': 'int',
            'suppressed_fail': 'int',
            'suppressed_warn': 'int',
            'suppressed_error': 'int',
            'new_1h_info': 'int',
            'new_1d_info': 'int',
            'new_1w_info': 'int',
            'old_info': 'int',
            'suppressed_info': 'int',
            'signature': 'Signature',
            'signature_id': 'int',
            'stat': 'Stat',
            'stat_id': 'int',
            'errors': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'new_1h_pass': 'new_1h_pass',
            'new_1d_pass': 'new_1d_pass',
            'new_1w_pass': 'new_1w_pass',
            'old_pass': 'old_pass',
            'new_1h_fail': 'new_1h_fail',
            'new_1d_fail': 'new_1d_fail',
            'new_1w_fail': 'new_1w_fail',
            'old_fail': 'old_fail',
            'new_1h_warn': 'new_1h_warn',
            'new_1d_warn': 'new_1d_warn',
            'new_1w_warn': 'new_1w_warn',
            'old_warn': 'old_warn',
            'new_1h_error': 'new_1h_error',
            'new_1d_error': 'new_1d_error',
            'new_1w_error': 'new_1w_error',
            'old_error': 'old_error',
            'suppressed_pass': 'suppressed_pass',
            'suppressed_fail': 'suppressed_fail',
            'suppressed_warn': 'suppressed_warn',
            'suppressed_error': 'suppressed_error',
            'new_1h_info': 'new_1h_info',
            'new_1d_info': 'new_1d_info',
            'new_1w_info': 'new_1w_info',
            'old_info': 'old_info',
            'suppressed_info': 'suppressed_info',
            'signature': 'signature',
            'signature_id': 'signature_id',
            'stat': 'stat',
            'stat_id': 'stat_id',
            'errors': 'errors'
        }

        self._id = id
        self._new_1h_pass = new_1h_pass
        self._new_1d_pass = new_1d_pass
        self._new_1w_pass = new_1w_pass
        self._old_pass = old_pass
        self._new_1h_fail = new_1h_fail
        self._new_1d_fail = new_1d_fail
        self._new_1w_fail = new_1w_fail
        self._old_fail = old_fail
        self._new_1h_warn = new_1h_warn
        self._new_1d_warn = new_1d_warn
        self._new_1w_warn = new_1w_warn
        self._old_warn = old_warn
        self._new_1h_error = new_1h_error
        self._new_1d_error = new_1d_error
        self._new_1w_error = new_1w_error
        self._old_error = old_error
        self._suppressed_pass = suppressed_pass
        self._suppressed_fail = suppressed_fail
        self._suppressed_warn = suppressed_warn
        self._suppressed_error = suppressed_error
        self._new_1h_info = new_1h_info
        self._new_1d_info = new_1d_info
        self._new_1w_info = new_1w_info
        self._old_info = old_info
        self._suppressed_info = suppressed_info
        self._signature = signature
        self._signature_id = signature_id
        self._stat = stat
        self._stat_id = stat_id
        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this StatSignatures.
        Unique ID

        :return: The id of this StatSignatures.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StatSignatures.
        Unique ID

        :param id: The id of this StatSignatures.
        :type: int
        """

        self._id = id

    @property
    def new_1h_pass(self):
        """
        Gets the new_1h_pass of this StatSignatures.

        :return: The new_1h_pass of this StatSignatures.
        :rtype: int
        """
        return self._new_1h_pass

    @new_1h_pass.setter
    def new_1h_pass(self, new_1h_pass):
        """
        Sets the new_1h_pass of this StatSignatures.

        :param new_1h_pass: The new_1h_pass of this StatSignatures.
        :type: int
        """

        self._new_1h_pass = new_1h_pass

    @property
    def new_1d_pass(self):
        """
        Gets the new_1d_pass of this StatSignatures.

        :return: The new_1d_pass of this StatSignatures.
        :rtype: int
        """
        return self._new_1d_pass

    @new_1d_pass.setter
    def new_1d_pass(self, new_1d_pass):
        """
        Sets the new_1d_pass of this StatSignatures.

        :param new_1d_pass: The new_1d_pass of this StatSignatures.
        :type: int
        """

        self._new_1d_pass = new_1d_pass

    @property
    def new_1w_pass(self):
        """
        Gets the new_1w_pass of this StatSignatures.

        :return: The new_1w_pass of this StatSignatures.
        :rtype: int
        """
        return self._new_1w_pass

    @new_1w_pass.setter
    def new_1w_pass(self, new_1w_pass):
        """
        Sets the new_1w_pass of this StatSignatures.

        :param new_1w_pass: The new_1w_pass of this StatSignatures.
        :type: int
        """

        self._new_1w_pass = new_1w_pass

    @property
    def old_pass(self):
        """
        Gets the old_pass of this StatSignatures.

        :return: The old_pass of this StatSignatures.
        :rtype: int
        """
        return self._old_pass

    @old_pass.setter
    def old_pass(self, old_pass):
        """
        Sets the old_pass of this StatSignatures.

        :param old_pass: The old_pass of this StatSignatures.
        :type: int
        """

        self._old_pass = old_pass

    @property
    def new_1h_fail(self):
        """
        Gets the new_1h_fail of this StatSignatures.

        :return: The new_1h_fail of this StatSignatures.
        :rtype: int
        """
        return self._new_1h_fail

    @new_1h_fail.setter
    def new_1h_fail(self, new_1h_fail):
        """
        Sets the new_1h_fail of this StatSignatures.

        :param new_1h_fail: The new_1h_fail of this StatSignatures.
        :type: int
        """

        self._new_1h_fail = new_1h_fail

    @property
    def new_1d_fail(self):
        """
        Gets the new_1d_fail of this StatSignatures.

        :return: The new_1d_fail of this StatSignatures.
        :rtype: int
        """
        return self._new_1d_fail

    @new_1d_fail.setter
    def new_1d_fail(self, new_1d_fail):
        """
        Sets the new_1d_fail of this StatSignatures.

        :param new_1d_fail: The new_1d_fail of this StatSignatures.
        :type: int
        """

        self._new_1d_fail = new_1d_fail

    @property
    def new_1w_fail(self):
        """
        Gets the new_1w_fail of this StatSignatures.

        :return: The new_1w_fail of this StatSignatures.
        :rtype: int
        """
        return self._new_1w_fail

    @new_1w_fail.setter
    def new_1w_fail(self, new_1w_fail):
        """
        Sets the new_1w_fail of this StatSignatures.

        :param new_1w_fail: The new_1w_fail of this StatSignatures.
        :type: int
        """

        self._new_1w_fail = new_1w_fail

    @property
    def old_fail(self):
        """
        Gets the old_fail of this StatSignatures.

        :return: The old_fail of this StatSignatures.
        :rtype: int
        """
        return self._old_fail

    @old_fail.setter
    def old_fail(self, old_fail):
        """
        Sets the old_fail of this StatSignatures.

        :param old_fail: The old_fail of this StatSignatures.
        :type: int
        """

        self._old_fail = old_fail

    @property
    def new_1h_warn(self):
        """
        Gets the new_1h_warn of this StatSignatures.

        :return: The new_1h_warn of this StatSignatures.
        :rtype: int
        """
        return self._new_1h_warn

    @new_1h_warn.setter
    def new_1h_warn(self, new_1h_warn):
        """
        Sets the new_1h_warn of this StatSignatures.

        :param new_1h_warn: The new_1h_warn of this StatSignatures.
        :type: int
        """

        self._new_1h_warn = new_1h_warn

    @property
    def new_1d_warn(self):
        """
        Gets the new_1d_warn of this StatSignatures.

        :return: The new_1d_warn of this StatSignatures.
        :rtype: int
        """
        return self._new_1d_warn

    @new_1d_warn.setter
    def new_1d_warn(self, new_1d_warn):
        """
        Sets the new_1d_warn of this StatSignatures.

        :param new_1d_warn: The new_1d_warn of this StatSignatures.
        :type: int
        """

        self._new_1d_warn = new_1d_warn

    @property
    def new_1w_warn(self):
        """
        Gets the new_1w_warn of this StatSignatures.

        :return: The new_1w_warn of this StatSignatures.
        :rtype: int
        """
        return self._new_1w_warn

    @new_1w_warn.setter
    def new_1w_warn(self, new_1w_warn):
        """
        Sets the new_1w_warn of this StatSignatures.

        :param new_1w_warn: The new_1w_warn of this StatSignatures.
        :type: int
        """

        self._new_1w_warn = new_1w_warn

    @property
    def old_warn(self):
        """
        Gets the old_warn of this StatSignatures.

        :return: The old_warn of this StatSignatures.
        :rtype: int
        """
        return self._old_warn

    @old_warn.setter
    def old_warn(self, old_warn):
        """
        Sets the old_warn of this StatSignatures.

        :param old_warn: The old_warn of this StatSignatures.
        :type: int
        """

        self._old_warn = old_warn

    @property
    def new_1h_error(self):
        """
        Gets the new_1h_error of this StatSignatures.

        :return: The new_1h_error of this StatSignatures.
        :rtype: int
        """
        return self._new_1h_error

    @new_1h_error.setter
    def new_1h_error(self, new_1h_error):
        """
        Sets the new_1h_error of this StatSignatures.

        :param new_1h_error: The new_1h_error of this StatSignatures.
        :type: int
        """

        self._new_1h_error = new_1h_error

    @property
    def new_1d_error(self):
        """
        Gets the new_1d_error of this StatSignatures.

        :return: The new_1d_error of this StatSignatures.
        :rtype: int
        """
        return self._new_1d_error

    @new_1d_error.setter
    def new_1d_error(self, new_1d_error):
        """
        Sets the new_1d_error of this StatSignatures.

        :param new_1d_error: The new_1d_error of this StatSignatures.
        :type: int
        """

        self._new_1d_error = new_1d_error

    @property
    def new_1w_error(self):
        """
        Gets the new_1w_error of this StatSignatures.

        :return: The new_1w_error of this StatSignatures.
        :rtype: int
        """
        return self._new_1w_error

    @new_1w_error.setter
    def new_1w_error(self, new_1w_error):
        """
        Sets the new_1w_error of this StatSignatures.

        :param new_1w_error: The new_1w_error of this StatSignatures.
        :type: int
        """

        self._new_1w_error = new_1w_error

    @property
    def old_error(self):
        """
        Gets the old_error of this StatSignatures.

        :return: The old_error of this StatSignatures.
        :rtype: int
        """
        return self._old_error

    @old_error.setter
    def old_error(self, old_error):
        """
        Sets the old_error of this StatSignatures.

        :param old_error: The old_error of this StatSignatures.
        :type: int
        """

        self._old_error = old_error

    @property
    def suppressed_pass(self):
        """
        Gets the suppressed_pass of this StatSignatures.

        :return: The suppressed_pass of this StatSignatures.
        :rtype: int
        """
        return self._suppressed_pass

    @suppressed_pass.setter
    def suppressed_pass(self, suppressed_pass):
        """
        Sets the suppressed_pass of this StatSignatures.

        :param suppressed_pass: The suppressed_pass of this StatSignatures.
        :type: int
        """

        self._suppressed_pass = suppressed_pass

    @property
    def suppressed_fail(self):
        """
        Gets the suppressed_fail of this StatSignatures.

        :return: The suppressed_fail of this StatSignatures.
        :rtype: int
        """
        return self._suppressed_fail

    @suppressed_fail.setter
    def suppressed_fail(self, suppressed_fail):
        """
        Sets the suppressed_fail of this StatSignatures.

        :param suppressed_fail: The suppressed_fail of this StatSignatures.
        :type: int
        """

        self._suppressed_fail = suppressed_fail

    @property
    def suppressed_warn(self):
        """
        Gets the suppressed_warn of this StatSignatures.

        :return: The suppressed_warn of this StatSignatures.
        :rtype: int
        """
        return self._suppressed_warn

    @suppressed_warn.setter
    def suppressed_warn(self, suppressed_warn):
        """
        Sets the suppressed_warn of this StatSignatures.

        :param suppressed_warn: The suppressed_warn of this StatSignatures.
        :type: int
        """

        self._suppressed_warn = suppressed_warn

    @property
    def suppressed_error(self):
        """
        Gets the suppressed_error of this StatSignatures.

        :return: The suppressed_error of this StatSignatures.
        :rtype: int
        """
        return self._suppressed_error

    @suppressed_error.setter
    def suppressed_error(self, suppressed_error):
        """
        Sets the suppressed_error of this StatSignatures.

        :param suppressed_error: The suppressed_error of this StatSignatures.
        :type: int
        """

        self._suppressed_error = suppressed_error

    @property
    def new_1h_info(self):
        """
        Gets the new_1h_info of this StatSignatures.

        :return: The new_1h_info of this StatSignatures.
        :rtype: int
        """
        return self._new_1h_info

    @new_1h_info.setter
    def new_1h_info(self, new_1h_info):
        """
        Sets the new_1h_info of this StatSignatures.

        :param new_1h_info: The new_1h_info of this StatSignatures.
        :type: int
        """

        self._new_1h_info = new_1h_info

    @property
    def new_1d_info(self):
        """
        Gets the new_1d_info of this StatSignatures.

        :return: The new_1d_info of this StatSignatures.
        :rtype: int
        """
        return self._new_1d_info

    @new_1d_info.setter
    def new_1d_info(self, new_1d_info):
        """
        Sets the new_1d_info of this StatSignatures.

        :param new_1d_info: The new_1d_info of this StatSignatures.
        :type: int
        """

        self._new_1d_info = new_1d_info

    @property
    def new_1w_info(self):
        """
        Gets the new_1w_info of this StatSignatures.

        :return: The new_1w_info of this StatSignatures.
        :rtype: int
        """
        return self._new_1w_info

    @new_1w_info.setter
    def new_1w_info(self, new_1w_info):
        """
        Sets the new_1w_info of this StatSignatures.

        :param new_1w_info: The new_1w_info of this StatSignatures.
        :type: int
        """

        self._new_1w_info = new_1w_info

    @property
    def old_info(self):
        """
        Gets the old_info of this StatSignatures.

        :return: The old_info of this StatSignatures.
        :rtype: int
        """
        return self._old_info

    @old_info.setter
    def old_info(self, old_info):
        """
        Sets the old_info of this StatSignatures.

        :param old_info: The old_info of this StatSignatures.
        :type: int
        """

        self._old_info = old_info

    @property
    def suppressed_info(self):
        """
        Gets the suppressed_info of this StatSignatures.

        :return: The suppressed_info of this StatSignatures.
        :rtype: int
        """
        return self._suppressed_info

    @suppressed_info.setter
    def suppressed_info(self, suppressed_info):
        """
        Sets the suppressed_info of this StatSignatures.

        :param suppressed_info: The suppressed_info of this StatSignatures.
        :type: int
        """

        self._suppressed_info = suppressed_info

    @property
    def signature(self):
        """
        Gets the signature of this StatSignatures.
        Associated Signature

        :return: The signature of this StatSignatures.
        :rtype: Signature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this StatSignatures.
        Associated Signature

        :param signature: The signature of this StatSignatures.
        :type: Signature
        """

        self._signature = signature

    @property
    def signature_id(self):
        """
        Gets the signature_id of this StatSignatures.
        Associated Signature Id

        :return: The signature_id of this StatSignatures.
        :rtype: int
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """
        Sets the signature_id of this StatSignatures.
        Associated Signature Id

        :param signature_id: The signature_id of this StatSignatures.
        :type: int
        """

        self._signature_id = signature_id

    @property
    def stat(self):
        """
        Gets the stat of this StatSignatures.
        Associated Stat

        :return: The stat of this StatSignatures.
        :rtype: Stat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """
        Sets the stat of this StatSignatures.
        Associated Stat

        :param stat: The stat of this StatSignatures.
        :type: Stat
        """

        self._stat = stat

    @property
    def stat_id(self):
        """
        Gets the stat_id of this StatSignatures.
        Associated Stat Id

        :return: The stat_id of this StatSignatures.
        :rtype: int
        """
        return self._stat_id

    @stat_id.setter
    def stat_id(self, stat_id):
        """
        Sets the stat_id of this StatSignatures.
        Associated Stat Id

        :param stat_id: The stat_id of this StatSignatures.
        :type: int
        """

        self._stat_id = stat_id

    @property
    def errors(self):
        """
        Gets the errors of this StatSignatures.
        Array of error messages if the request failed

        :return: The errors of this StatSignatures.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this StatSignatures.
        Array of error messages if the request failed

        :param errors: The errors of this StatSignatures.
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
        if not isinstance(other, StatSignatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
