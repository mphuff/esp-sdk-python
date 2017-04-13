# coding: utf-8

"""
    ESP Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class Suppression(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, relationships=None, errors=None, id=None, created_at=None, reason=None, resource=None, status=None, suppression_type=None, updated_at=None, organization=None, organization_id=None, created_by=None, created_by_id=None, external_accounts=None, external_account_ids=None, regions=None, region_ids=None, signatures=None, signature_ids=None, custom_signatures=None, custom_signature_ids=None):
        """
        Suppression - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'relationships': 'object',
            'errors': 'list[str]',
            'id': 'int',
            'created_at': 'datetime',
            'reason': 'str',
            'resource': 'str',
            'status': 'str',
            'suppression_type': 'str',
            'updated_at': 'datetime',
            'organization': 'Organization',
            'organization_id': 'int',
            'created_by': 'list[object]',
            'created_by_id': 'int',
            'external_accounts': 'list[ExternalAccount]',
            'external_account_ids': 'list[int]',
            'regions': 'list[Region]',
            'region_ids': 'list[int]',
            'signatures': 'list[Signature]',
            'signature_ids': 'list[int]',
            'custom_signatures': 'list[CustomSignature]',
            'custom_signature_ids': 'list[int]'
        }

        self.attribute_map = {
            'relationships': 'relationships',
            'errors': 'errors',
            'id': 'id',
            'created_at': 'created_at',
            'reason': 'reason',
            'resource': 'resource',
            'status': 'status',
            'suppression_type': 'suppression_type',
            'updated_at': 'updated_at',
            'organization': 'organization',
            'organization_id': 'organization_id',
            'created_by': 'created_by',
            'created_by_id': 'created_by_id',
            'external_accounts': 'external_accounts',
            'external_account_ids': 'external_account_ids',
            'regions': 'regions',
            'region_ids': 'region_ids',
            'signatures': 'signatures',
            'signature_ids': 'signature_ids',
            'custom_signatures': 'custom_signatures',
            'custom_signature_ids': 'custom_signature_ids'
        }

        self._relationships = relationships
        self._errors = errors
        self._id = id
        self._created_at = created_at
        self._reason = reason
        self._resource = resource
        self._status = status
        self._suppression_type = suppression_type
        self._updated_at = updated_at
        self._organization = organization
        self._organization_id = organization_id
        self._created_by = created_by
        self._created_by_id = created_by_id
        self._external_accounts = external_accounts
        self._external_account_ids = external_account_ids
        self._regions = regions
        self._region_ids = region_ids
        self._signatures = signatures
        self._signature_ids = signature_ids
        self._custom_signatures = custom_signatures
        self._custom_signature_ids = custom_signature_ids

    @property
    def relationships(self):
        """
        Gets the relationships of this Suppression.
        Links to Associated Objects

        :return: The relationships of this Suppression.
        :rtype: object
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Suppression.
        Links to Associated Objects

        :param relationships: The relationships of this Suppression.
        :type: object
        """

        self._relationships = relationships

    @property
    def errors(self):
        """
        Gets the errors of this Suppression.
        Array of error messages if the request failed

        :return: The errors of this Suppression.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this Suppression.
        Array of error messages if the request failed

        :param errors: The errors of this Suppression.
        :type: list[str]
        """

        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this Suppression.
        Unique ID

        :return: The id of this Suppression.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Suppression.
        Unique ID

        :param id: The id of this Suppression.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Suppression.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Suppression.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Suppression.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Suppression.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def reason(self):
        """
        Gets the reason of this Suppression.
        The reason for the suppresion

        :return: The reason of this Suppression.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Suppression.
        The reason for the suppresion

        :param reason: The reason of this Suppression.
        :type: str
        """

        self._reason = reason

    @property
    def resource(self):
        """
        Gets the resource of this Suppression.
        The resource string this suppression will suppress alerts for

        :return: The resource of this Suppression.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this Suppression.
        The resource string this suppression will suppress alerts for

        :param resource: The resource of this Suppression.
        :type: str
        """

        self._resource = resource

    @property
    def status(self):
        """
        Gets the status of this Suppression.
        The status of this suppresion

        :return: The status of this Suppression.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Suppression.
        The status of this suppresion

        :param status: The status of this Suppression.
        :type: str
        """

        self._status = status

    @property
    def suppression_type(self):
        """
        Gets the suppression_type of this Suppression.
        Type of suppression. Possible values are unique_identifiers, regions, and signatures

        :return: The suppression_type of this Suppression.
        :rtype: str
        """
        return self._suppression_type

    @suppression_type.setter
    def suppression_type(self, suppression_type):
        """
        Sets the suppression_type of this Suppression.
        Type of suppression. Possible values are unique_identifiers, regions, and signatures

        :param suppression_type: The suppression_type of this Suppression.
        :type: str
        """

        self._suppression_type = suppression_type

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Suppression.
        ISO 8601 timestamp when the suppression was last updated

        :return: The updated_at of this Suppression.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Suppression.
        ISO 8601 timestamp when the suppression was last updated

        :param updated_at: The updated_at of this Suppression.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def organization(self):
        """
        Gets the organization of this Suppression.
        Associated Organization

        :return: The organization of this Suppression.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Suppression.
        Associated Organization

        :param organization: The organization of this Suppression.
        :type: Organization
        """

        self._organization = organization

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Suppression.
        Associated Organization Id

        :return: The organization_id of this Suppression.
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Suppression.
        Associated Organization Id

        :param organization_id: The organization_id of this Suppression.
        :type: int
        """

        self._organization_id = organization_id

    @property
    def created_by(self):
        """
        Gets the created_by of this Suppression.
        User That Created This Suppression

        :return: The created_by of this Suppression.
        :rtype: list[object]
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Suppression.
        User That Created This Suppression

        :param created_by: The created_by of this Suppression.
        :type: list[object]
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Suppression.
        User That Created This Suppression's Id

        :return: The created_by_id of this Suppression.
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Suppression.
        User That Created This Suppression's Id

        :param created_by_id: The created_by_id of this Suppression.
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def external_accounts(self):
        """
        Gets the external_accounts of this Suppression.
        Associated External Accounts

        :return: The external_accounts of this Suppression.
        :rtype: list[ExternalAccount]
        """
        return self._external_accounts

    @external_accounts.setter
    def external_accounts(self, external_accounts):
        """
        Sets the external_accounts of this Suppression.
        Associated External Accounts

        :param external_accounts: The external_accounts of this Suppression.
        :type: list[ExternalAccount]
        """

        self._external_accounts = external_accounts

    @property
    def external_account_ids(self):
        """
        Gets the external_account_ids of this Suppression.
        Associated External Account Ids

        :return: The external_account_ids of this Suppression.
        :rtype: list[int]
        """
        return self._external_account_ids

    @external_account_ids.setter
    def external_account_ids(self, external_account_ids):
        """
        Sets the external_account_ids of this Suppression.
        Associated External Account Ids

        :param external_account_ids: The external_account_ids of this Suppression.
        :type: list[int]
        """

        self._external_account_ids = external_account_ids

    @property
    def regions(self):
        """
        Gets the regions of this Suppression.
        Associated Regions

        :return: The regions of this Suppression.
        :rtype: list[Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this Suppression.
        Associated Regions

        :param regions: The regions of this Suppression.
        :type: list[Region]
        """

        self._regions = regions

    @property
    def region_ids(self):
        """
        Gets the region_ids of this Suppression.
        Associated Region Ids

        :return: The region_ids of this Suppression.
        :rtype: list[int]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        """
        Sets the region_ids of this Suppression.
        Associated Region Ids

        :param region_ids: The region_ids of this Suppression.
        :type: list[int]
        """

        self._region_ids = region_ids

    @property
    def signatures(self):
        """
        Gets the signatures of this Suppression.
        Associated Signatures

        :return: The signatures of this Suppression.
        :rtype: list[Signature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this Suppression.
        Associated Signatures

        :param signatures: The signatures of this Suppression.
        :type: list[Signature]
        """

        self._signatures = signatures

    @property
    def signature_ids(self):
        """
        Gets the signature_ids of this Suppression.
        Associated Signature Ids

        :return: The signature_ids of this Suppression.
        :rtype: list[int]
        """
        return self._signature_ids

    @signature_ids.setter
    def signature_ids(self, signature_ids):
        """
        Sets the signature_ids of this Suppression.
        Associated Signature Ids

        :param signature_ids: The signature_ids of this Suppression.
        :type: list[int]
        """

        self._signature_ids = signature_ids

    @property
    def custom_signatures(self):
        """
        Gets the custom_signatures of this Suppression.
        Associated Custom Signatures

        :return: The custom_signatures of this Suppression.
        :rtype: list[CustomSignature]
        """
        return self._custom_signatures

    @custom_signatures.setter
    def custom_signatures(self, custom_signatures):
        """
        Sets the custom_signatures of this Suppression.
        Associated Custom Signatures

        :param custom_signatures: The custom_signatures of this Suppression.
        :type: list[CustomSignature]
        """

        self._custom_signatures = custom_signatures

    @property
    def custom_signature_ids(self):
        """
        Gets the custom_signature_ids of this Suppression.
        Associated Custom Signature Ids

        :return: The custom_signature_ids of this Suppression.
        :rtype: list[int]
        """
        return self._custom_signature_ids

    @custom_signature_ids.setter
    def custom_signature_ids(self, custom_signature_ids):
        """
        Sets the custom_signature_ids of this Suppression.
        Associated Custom Signature Ids

        :param custom_signature_ids: The custom_signature_ids of this Suppression.
        :type: list[int]
        """

        self._custom_signature_ids = custom_signature_ids

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
        if not isinstance(other, Suppression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other