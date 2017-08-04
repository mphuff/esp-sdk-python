# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.models.custom_signature_result import CustomSignatureResult


class TestCustomSignatureResult(unittest.TestCase):
    """ CustomSignatureResult unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomSignatureResult(self):
        """
        Test CustomSignatureResult
        """
        model = esp_sdk.models.custom_signature_result.CustomSignatureResult()


if __name__ == '__main__':
    unittest.main()
