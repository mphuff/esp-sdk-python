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


class ComplianceControl(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, name=None, identifier=None, description=None, updated_at=None, position=None, compliance_standard=None, compliance_standard_id=None, compliance_domain=None, compliance_domain_id=None, signatures=None, signature_ids=None, errors=None):
        """
        ComplianceControl - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'created_at': 'datetime',
            'name': 'str',
            'identifier': 'str',
            'description': 'str',
            'updated_at': 'datetime',
            'position': 'int',
            'compliance_standard': 'ComplianceStandard',
            'compliance_standard_id': 'int',
            'compliance_domain': 'ComplianceDomain',
            'compliance_domain_id': 'int',
            'signatures': 'list[Signature]',
            'signature_ids': 'list[int]',
            'errors': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'name': 'name',
            'identifier': 'identifier',
            'description': 'description',
            'updated_at': 'updated_at',
            'position': 'position',
            'compliance_standard': 'compliance_standard',
            'compliance_standard_id': 'compliance_standard_id',
            'compliance_domain': 'compliance_domain',
            'compliance_domain_id': 'compliance_domain_id',
            'signatures': 'signatures',
            'signature_ids': 'signature_ids',
            'errors': 'errors'
        }

        self._id = id
        self._created_at = created_at
        self._name = name
        self._identifier = identifier
        self._description = description
        self._updated_at = updated_at
        self._position = position
        self._compliance_standard = compliance_standard
        self._compliance_standard_id = compliance_standard_id
        self._compliance_domain = compliance_domain
        self._compliance_domain_id = compliance_domain_id
        self._signatures = signatures
        self._signature_ids = signature_ids
        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this ComplianceControl.
        Unique ID

        :return: The id of this ComplianceControl.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComplianceControl.
        Unique ID

        :param id: The id of this ComplianceControl.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this ComplianceControl.
        Created At

        :return: The created_at of this ComplianceControl.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ComplianceControl.
        Created At

        :param created_at: The created_at of this ComplianceControl.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """
        Gets the name of this ComplianceControl.
        Name

        :return: The name of this ComplianceControl.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ComplianceControl.
        Name

        :param name: The name of this ComplianceControl.
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this ComplianceControl.
        The identifier of this control

        :return: The identifier of this ComplianceControl.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ComplianceControl.
        The identifier of this control

        :param identifier: The identifier of this ComplianceControl.
        :type: str
        """

        self._identifier = identifier

    @property
    def description(self):
        """
        Gets the description of this ComplianceControl.
        The description for this control

        :return: The description of this ComplianceControl.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ComplianceControl.
        The description for this control

        :param description: The description of this ComplianceControl.
        :type: str
        """

        self._description = description

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ComplianceControl.
        Updated At

        :return: The updated_at of this ComplianceControl.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ComplianceControl.
        Updated At

        :param updated_at: The updated_at of this ComplianceControl.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def position(self):
        """
        Gets the position of this ComplianceControl.
        The position of this control within the Domain

        :return: The position of this ComplianceControl.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ComplianceControl.
        The position of this control within the Domain

        :param position: The position of this ComplianceControl.
        :type: int
        """

        self._position = position

    @property
    def compliance_standard(self):
        """
        Gets the compliance_standard of this ComplianceControl.
        Associated Compliance Standard

        :return: The compliance_standard of this ComplianceControl.
        :rtype: ComplianceStandard
        """
        return self._compliance_standard

    @compliance_standard.setter
    def compliance_standard(self, compliance_standard):
        """
        Sets the compliance_standard of this ComplianceControl.
        Associated Compliance Standard

        :param compliance_standard: The compliance_standard of this ComplianceControl.
        :type: ComplianceStandard
        """

        self._compliance_standard = compliance_standard

    @property
    def compliance_standard_id(self):
        """
        Gets the compliance_standard_id of this ComplianceControl.
        Associated Compliance Standard Id

        :return: The compliance_standard_id of this ComplianceControl.
        :rtype: int
        """
        return self._compliance_standard_id

    @compliance_standard_id.setter
    def compliance_standard_id(self, compliance_standard_id):
        """
        Sets the compliance_standard_id of this ComplianceControl.
        Associated Compliance Standard Id

        :param compliance_standard_id: The compliance_standard_id of this ComplianceControl.
        :type: int
        """

        self._compliance_standard_id = compliance_standard_id

    @property
    def compliance_domain(self):
        """
        Gets the compliance_domain of this ComplianceControl.
        Associated Compliance Domain

        :return: The compliance_domain of this ComplianceControl.
        :rtype: ComplianceDomain
        """
        return self._compliance_domain

    @compliance_domain.setter
    def compliance_domain(self, compliance_domain):
        """
        Sets the compliance_domain of this ComplianceControl.
        Associated Compliance Domain

        :param compliance_domain: The compliance_domain of this ComplianceControl.
        :type: ComplianceDomain
        """

        self._compliance_domain = compliance_domain

    @property
    def compliance_domain_id(self):
        """
        Gets the compliance_domain_id of this ComplianceControl.
        Associated Compliance Domain Id

        :return: The compliance_domain_id of this ComplianceControl.
        :rtype: int
        """
        return self._compliance_domain_id

    @compliance_domain_id.setter
    def compliance_domain_id(self, compliance_domain_id):
        """
        Sets the compliance_domain_id of this ComplianceControl.
        Associated Compliance Domain Id

        :param compliance_domain_id: The compliance_domain_id of this ComplianceControl.
        :type: int
        """

        self._compliance_domain_id = compliance_domain_id

    @property
    def signatures(self):
        """
        Gets the signatures of this ComplianceControl.
        Associated Signatures

        :return: The signatures of this ComplianceControl.
        :rtype: list[Signature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this ComplianceControl.
        Associated Signatures

        :param signatures: The signatures of this ComplianceControl.
        :type: list[Signature]
        """

        self._signatures = signatures

    @property
    def signature_ids(self):
        """
        Gets the signature_ids of this ComplianceControl.
        Associated Signatures Ids

        :return: The signature_ids of this ComplianceControl.
        :rtype: list[int]
        """
        return self._signature_ids

    @signature_ids.setter
    def signature_ids(self, signature_ids):
        """
        Sets the signature_ids of this ComplianceControl.
        Associated Signatures Ids

        :param signature_ids: The signature_ids of this ComplianceControl.
        :type: list[int]
        """

        self._signature_ids = signature_ids

    @property
    def errors(self):
        """
        Gets the errors of this ComplianceControl.
        Array of error messages if the request failed

        :return: The errors of this ComplianceControl.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ComplianceControl.
        Array of error messages if the request failed

        :param errors: The errors of this ComplianceControl.
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
        if not isinstance(other, ComplianceControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
