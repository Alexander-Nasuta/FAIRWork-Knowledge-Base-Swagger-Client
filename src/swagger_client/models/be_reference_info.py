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

class BeReferenceInfo(object):
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
        'by_user': 'str',
        'caption': 'str',
        'created': 'str',
        'from_group': 'str',
        'instance_id': 'int',
        'parent_child': 'str',
        'related': 'BreakdownElementInfo',
        'remark': 'str',
        'role': 'str'
    }

    attribute_map = {
        'by_user': 'by_user',
        'caption': 'caption',
        'created': 'created',
        'from_group': 'from_group',
        'instance_id': 'instance_id',
        'parent_child': 'parent_child',
        'related': 'related',
        'remark': 'remark',
        'role': 'role'
    }

    def __init__(self, by_user=None, caption=None, created=None, from_group=None, instance_id=None, parent_child=None, related=None, remark=None, role=None):  # noqa: E501
        """BeReferenceInfo - a model defined in Swagger"""  # noqa: E501
        self._by_user = None
        self._caption = None
        self._created = None
        self._from_group = None
        self._instance_id = None
        self._parent_child = None
        self._related = None
        self._remark = None
        self._role = None
        self.discriminator = None
        if by_user is not None:
            self.by_user = by_user
        if caption is not None:
            self.caption = caption
        if created is not None:
            self.created = created
        if from_group is not None:
            self.from_group = from_group
        if instance_id is not None:
            self.instance_id = instance_id
        if parent_child is not None:
            self.parent_child = parent_child
        if related is not None:
            self.related = related
        if remark is not None:
            self.remark = remark
        if role is not None:
            self.role = role

    @property
    def by_user(self):
        """Gets the by_user of this BeReferenceInfo.  # noqa: E501


        :return: The by_user of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._by_user

    @by_user.setter
    def by_user(self, by_user):
        """Sets the by_user of this BeReferenceInfo.


        :param by_user: The by_user of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._by_user = by_user

    @property
    def caption(self):
        """Gets the caption of this BeReferenceInfo.  # noqa: E501


        :return: The caption of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this BeReferenceInfo.


        :param caption: The caption of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def created(self):
        """Gets the created of this BeReferenceInfo.  # noqa: E501


        :return: The created of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BeReferenceInfo.


        :param created: The created of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def from_group(self):
        """Gets the from_group of this BeReferenceInfo.  # noqa: E501


        :return: The from_group of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._from_group

    @from_group.setter
    def from_group(self, from_group):
        """Sets the from_group of this BeReferenceInfo.


        :param from_group: The from_group of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._from_group = from_group

    @property
    def instance_id(self):
        """Gets the instance_id of this BeReferenceInfo.  # noqa: E501


        :return: The instance_id of this BeReferenceInfo.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BeReferenceInfo.


        :param instance_id: The instance_id of this BeReferenceInfo.  # noqa: E501
        :type: int
        """

        self._instance_id = instance_id

    @property
    def parent_child(self):
        """Gets the parent_child of this BeReferenceInfo.  # noqa: E501


        :return: The parent_child of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_child

    @parent_child.setter
    def parent_child(self, parent_child):
        """Sets the parent_child of this BeReferenceInfo.


        :param parent_child: The parent_child of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._parent_child = parent_child

    @property
    def related(self):
        """Gets the related of this BeReferenceInfo.  # noqa: E501


        :return: The related of this BeReferenceInfo.  # noqa: E501
        :rtype: BreakdownElementInfo
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this BeReferenceInfo.


        :param related: The related of this BeReferenceInfo.  # noqa: E501
        :type: BreakdownElementInfo
        """

        self._related = related

    @property
    def remark(self):
        """Gets the remark of this BeReferenceInfo.  # noqa: E501


        :return: The remark of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BeReferenceInfo.


        :param remark: The remark of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def role(self):
        """Gets the role of this BeReferenceInfo.  # noqa: E501


        :return: The role of this BeReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this BeReferenceInfo.


        :param role: The role of this BeReferenceInfo.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(BeReferenceInfo, dict):
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
        if not isinstance(other, BeReferenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
