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

class ConceptTreeView(object):
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
        'children': 'list[ConceptTreeView]',
        'description': 'str',
        'domain': 'str',
        'name': 'str',
        'urn': 'str'
    }

    attribute_map = {
        'children': 'children',
        'description': 'description',
        'domain': 'domain',
        'name': 'name',
        'urn': 'urn'
    }

    def __init__(self, children=None, description=None, domain=None, name=None, urn=None):  # noqa: E501
        """ConceptTreeView - a model defined in Swagger"""  # noqa: E501
        self._children = None
        self._description = None
        self._domain = None
        self._name = None
        self._urn = None
        self.discriminator = None
        if children is not None:
            self.children = children
        if description is not None:
            self.description = description
        if domain is not None:
            self.domain = domain
        if name is not None:
            self.name = name
        if urn is not None:
            self.urn = urn

    @property
    def children(self):
        """Gets the children of this ConceptTreeView.  # noqa: E501


        :return: The children of this ConceptTreeView.  # noqa: E501
        :rtype: list[ConceptTreeView]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ConceptTreeView.


        :param children: The children of this ConceptTreeView.  # noqa: E501
        :type: list[ConceptTreeView]
        """

        self._children = children

    @property
    def description(self):
        """Gets the description of this ConceptTreeView.  # noqa: E501


        :return: The description of this ConceptTreeView.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConceptTreeView.


        :param description: The description of this ConceptTreeView.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def domain(self):
        """Gets the domain of this ConceptTreeView.  # noqa: E501


        :return: The domain of this ConceptTreeView.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ConceptTreeView.


        :param domain: The domain of this ConceptTreeView.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def name(self):
        """Gets the name of this ConceptTreeView.  # noqa: E501


        :return: The name of this ConceptTreeView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConceptTreeView.


        :param name: The name of this ConceptTreeView.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def urn(self):
        """Gets the urn of this ConceptTreeView.  # noqa: E501


        :return: The urn of this ConceptTreeView.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this ConceptTreeView.


        :param urn: The urn of this ConceptTreeView.  # noqa: E501
        :type: str
        """

        self._urn = urn

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
        if issubclass(ConceptTreeView, dict):
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
        if not isinstance(other, ConceptTreeView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other