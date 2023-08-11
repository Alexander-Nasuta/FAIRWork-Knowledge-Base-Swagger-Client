# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LoginRez(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'str',
        'name': 'str',
        'token': 'str',
        'use2_fa': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'name': 'name',
        'token': 'token',
        'use2_fa': 'use2FA'
    }

    def __init__(self, error=None, name=None, token=None, use2_fa=None):  # noqa: E501
        """LoginRez - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._name = None
        self._token = None
        self._use2_fa = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if name is not None:
            self.name = name
        if token is not None:
            self.token = token
        if use2_fa is not None:
            self.use2_fa = use2_fa

    @property
    def error(self):
        """Gets the error of this LoginRez.  # noqa: E501


        :return: The error of this LoginRez.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LoginRez.


        :param error: The error of this LoginRez.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def name(self):
        """Gets the name of this LoginRez.  # noqa: E501


        :return: The name of this LoginRez.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoginRez.


        :param name: The name of this LoginRez.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def token(self):
        """Gets the token of this LoginRez.  # noqa: E501


        :return: The token of this LoginRez.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this LoginRez.


        :param token: The token of this LoginRez.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def use2_fa(self):
        """Gets the use2_fa of this LoginRez.  # noqa: E501


        :return: The use2_fa of this LoginRez.  # noqa: E501
        :rtype: bool
        """
        return self._use2_fa

    @use2_fa.setter
    def use2_fa(self, use2_fa):
        """Sets the use2_fa of this LoginRez.


        :param use2_fa: The use2_fa of this LoginRez.  # noqa: E501
        :type: bool
        """

        self._use2_fa = use2_fa

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(LoginRez, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginRez):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other