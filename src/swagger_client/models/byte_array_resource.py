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

class ByteArrayResource(object):
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
        'byte_array': 'str',
        'description': 'str'
    }

    attribute_map = {
        'byte_array': 'byteArray',
        'description': 'description'
    }

    def __init__(self, byte_array=None, description=None):  # noqa: E501
        """ByteArrayResource - a model defined in Swagger"""  # noqa: E501
        self._byte_array = None
        self._description = None
        self.discriminator = None
        if byte_array is not None:
            self.byte_array = byte_array
        if description is not None:
            self.description = description

    @property
    def byte_array(self):
        """Gets the byte_array of this ByteArrayResource.  # noqa: E501


        :return: The byte_array of this ByteArrayResource.  # noqa: E501
        :rtype: str
        """
        return self._byte_array

    @byte_array.setter
    def byte_array(self, byte_array):
        """Sets the byte_array of this ByteArrayResource.


        :param byte_array: The byte_array of this ByteArrayResource.  # noqa: E501
        :type: str
        """

        self._byte_array = byte_array

    @property
    def description(self):
        """Gets the description of this ByteArrayResource.  # noqa: E501


        :return: The description of this ByteArrayResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ByteArrayResource.


        :param description: The description of this ByteArrayResource.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ByteArrayResource, dict):
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
        if not isinstance(other, ByteArrayResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
