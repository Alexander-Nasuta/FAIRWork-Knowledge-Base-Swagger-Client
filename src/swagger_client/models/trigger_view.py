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

class TriggerView(object):
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
        'action': 'ActionView',
        'active': 'bool',
        'author': 'str',
        'condition': 'str',
        'event_types': 'list[EventTypeView]',
        'id': 'int',
        'name': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'action': 'action',
        'active': 'active',
        'author': 'author',
        'condition': 'condition',
        'event_types': 'event_types',
        'id': 'id',
        'name': 'name',
        'timestamp': 'timestamp'
    }

    def __init__(self, action=None, active=None, author=None, condition=None, event_types=None, id=None, name=None, timestamp=None):  # noqa: E501
        """TriggerView - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._active = None
        self._author = None
        self._condition = None
        self._event_types = None
        self._id = None
        self._name = None
        self._timestamp = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if active is not None:
            self.active = active
        if author is not None:
            self.author = author
        if condition is not None:
            self.condition = condition
        if event_types is not None:
            self.event_types = event_types
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def action(self):
        """Gets the action of this TriggerView.  # noqa: E501


        :return: The action of this TriggerView.  # noqa: E501
        :rtype: ActionView
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TriggerView.


        :param action: The action of this TriggerView.  # noqa: E501
        :type: ActionView
        """

        self._action = action

    @property
    def active(self):
        """Gets the active of this TriggerView.  # noqa: E501


        :return: The active of this TriggerView.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TriggerView.


        :param active: The active of this TriggerView.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def author(self):
        """Gets the author of this TriggerView.  # noqa: E501


        :return: The author of this TriggerView.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TriggerView.


        :param author: The author of this TriggerView.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def condition(self):
        """Gets the condition of this TriggerView.  # noqa: E501


        :return: The condition of this TriggerView.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this TriggerView.


        :param condition: The condition of this TriggerView.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def event_types(self):
        """Gets the event_types of this TriggerView.  # noqa: E501


        :return: The event_types of this TriggerView.  # noqa: E501
        :rtype: list[EventTypeView]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this TriggerView.


        :param event_types: The event_types of this TriggerView.  # noqa: E501
        :type: list[EventTypeView]
        """

        self._event_types = event_types

    @property
    def id(self):
        """Gets the id of this TriggerView.  # noqa: E501


        :return: The id of this TriggerView.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TriggerView.


        :param id: The id of this TriggerView.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TriggerView.  # noqa: E501


        :return: The name of this TriggerView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TriggerView.


        :param name: The name of this TriggerView.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this TriggerView.  # noqa: E501


        :return: The timestamp of this TriggerView.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TriggerView.


        :param timestamp: The timestamp of this TriggerView.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(TriggerView, dict):
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
        if not isinstance(other, TriggerView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
