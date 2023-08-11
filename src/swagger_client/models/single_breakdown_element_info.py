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

class SingleBreakdownElementInfo(object):
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
        'bkd_version_id': 'str',
        'element': 'BreakdownElementInfo'
    }

    attribute_map = {
        'bkd_version_id': 'bkd_version_id',
        'element': 'element'
    }

    def __init__(self, bkd_version_id=None, element=None):  # noqa: E501
        """SingleBreakdownElementInfo - a model defined in Swagger"""  # noqa: E501
        self._bkd_version_id = None
        self._element = None
        self.discriminator = None
        if bkd_version_id is not None:
            self.bkd_version_id = bkd_version_id
        if element is not None:
            self.element = element

    @property
    def bkd_version_id(self):
        """Gets the bkd_version_id of this SingleBreakdownElementInfo.  # noqa: E501


        :return: The bkd_version_id of this SingleBreakdownElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkd_version_id

    @bkd_version_id.setter
    def bkd_version_id(self, bkd_version_id):
        """Sets the bkd_version_id of this SingleBreakdownElementInfo.


        :param bkd_version_id: The bkd_version_id of this SingleBreakdownElementInfo.  # noqa: E501
        :type: str
        """

        self._bkd_version_id = bkd_version_id

    @property
    def element(self):
        """Gets the element of this SingleBreakdownElementInfo.  # noqa: E501


        :return: The element of this SingleBreakdownElementInfo.  # noqa: E501
        :rtype: BreakdownElementInfo
        """
        return self._element

    @element.setter
    def element(self, element):
        """Sets the element of this SingleBreakdownElementInfo.


        :param element: The element of this SingleBreakdownElementInfo.  # noqa: E501
        :type: BreakdownElementInfo
        """

        self._element = element

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
        if issubclass(SingleBreakdownElementInfo, dict):
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
        if not isinstance(other, SingleBreakdownElementInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
