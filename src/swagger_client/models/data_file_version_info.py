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

class DataFileVersionInfo(object):
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
        'affected_by_documents': 'list[DataFileTreePathInfo]',
        'affects_documents': 'list[DataFileTreePathInfo]',
        'changes_description': 'str',
        'date_submitted': 'str',
        'instance_id': 'int',
        'phase': 'str',
        'status': 'str',
        'sticky_notes': 'list[StickyNoteInfo]',
        'submitted_by_user': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'affected_by_documents': 'affected_by_documents',
        'affects_documents': 'affects_documents',
        'changes_description': 'changes_description',
        'date_submitted': 'date_submitted',
        'instance_id': 'instance_id',
        'phase': 'phase',
        'status': 'status',
        'sticky_notes': 'sticky_notes',
        'submitted_by_user': 'submitted_by_user',
        'version_id': 'version_id'
    }

    def __init__(self, affected_by_documents=None, affects_documents=None, changes_description=None, date_submitted=None, instance_id=None, phase=None, status=None, sticky_notes=None, submitted_by_user=None, version_id=None):  # noqa: E501
        """DataFileVersionInfo - a model defined in Swagger"""  # noqa: E501
        self._affected_by_documents = None
        self._affects_documents = None
        self._changes_description = None
        self._date_submitted = None
        self._instance_id = None
        self._phase = None
        self._status = None
        self._sticky_notes = None
        self._submitted_by_user = None
        self._version_id = None
        self.discriminator = None
        if affected_by_documents is not None:
            self.affected_by_documents = affected_by_documents
        if affects_documents is not None:
            self.affects_documents = affects_documents
        if changes_description is not None:
            self.changes_description = changes_description
        if date_submitted is not None:
            self.date_submitted = date_submitted
        if instance_id is not None:
            self.instance_id = instance_id
        if phase is not None:
            self.phase = phase
        if status is not None:
            self.status = status
        if sticky_notes is not None:
            self.sticky_notes = sticky_notes
        if submitted_by_user is not None:
            self.submitted_by_user = submitted_by_user
        if version_id is not None:
            self.version_id = version_id

    @property
    def affected_by_documents(self):
        """Gets the affected_by_documents of this DataFileVersionInfo.  # noqa: E501


        :return: The affected_by_documents of this DataFileVersionInfo.  # noqa: E501
        :rtype: list[DataFileTreePathInfo]
        """
        return self._affected_by_documents

    @affected_by_documents.setter
    def affected_by_documents(self, affected_by_documents):
        """Sets the affected_by_documents of this DataFileVersionInfo.


        :param affected_by_documents: The affected_by_documents of this DataFileVersionInfo.  # noqa: E501
        :type: list[DataFileTreePathInfo]
        """

        self._affected_by_documents = affected_by_documents

    @property
    def affects_documents(self):
        """Gets the affects_documents of this DataFileVersionInfo.  # noqa: E501


        :return: The affects_documents of this DataFileVersionInfo.  # noqa: E501
        :rtype: list[DataFileTreePathInfo]
        """
        return self._affects_documents

    @affects_documents.setter
    def affects_documents(self, affects_documents):
        """Sets the affects_documents of this DataFileVersionInfo.


        :param affects_documents: The affects_documents of this DataFileVersionInfo.  # noqa: E501
        :type: list[DataFileTreePathInfo]
        """

        self._affects_documents = affects_documents

    @property
    def changes_description(self):
        """Gets the changes_description of this DataFileVersionInfo.  # noqa: E501


        :return: The changes_description of this DataFileVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._changes_description

    @changes_description.setter
    def changes_description(self, changes_description):
        """Sets the changes_description of this DataFileVersionInfo.


        :param changes_description: The changes_description of this DataFileVersionInfo.  # noqa: E501
        :type: str
        """

        self._changes_description = changes_description

    @property
    def date_submitted(self):
        """Gets the date_submitted of this DataFileVersionInfo.  # noqa: E501


        :return: The date_submitted of this DataFileVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._date_submitted

    @date_submitted.setter
    def date_submitted(self, date_submitted):
        """Sets the date_submitted of this DataFileVersionInfo.


        :param date_submitted: The date_submitted of this DataFileVersionInfo.  # noqa: E501
        :type: str
        """

        self._date_submitted = date_submitted

    @property
    def instance_id(self):
        """Gets the instance_id of this DataFileVersionInfo.  # noqa: E501


        :return: The instance_id of this DataFileVersionInfo.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DataFileVersionInfo.


        :param instance_id: The instance_id of this DataFileVersionInfo.  # noqa: E501
        :type: int
        """

        self._instance_id = instance_id

    @property
    def phase(self):
        """Gets the phase of this DataFileVersionInfo.  # noqa: E501


        :return: The phase of this DataFileVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this DataFileVersionInfo.


        :param phase: The phase of this DataFileVersionInfo.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def status(self):
        """Gets the status of this DataFileVersionInfo.  # noqa: E501


        :return: The status of this DataFileVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataFileVersionInfo.


        :param status: The status of this DataFileVersionInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sticky_notes(self):
        """Gets the sticky_notes of this DataFileVersionInfo.  # noqa: E501


        :return: The sticky_notes of this DataFileVersionInfo.  # noqa: E501
        :rtype: list[StickyNoteInfo]
        """
        return self._sticky_notes

    @sticky_notes.setter
    def sticky_notes(self, sticky_notes):
        """Sets the sticky_notes of this DataFileVersionInfo.


        :param sticky_notes: The sticky_notes of this DataFileVersionInfo.  # noqa: E501
        :type: list[StickyNoteInfo]
        """

        self._sticky_notes = sticky_notes

    @property
    def submitted_by_user(self):
        """Gets the submitted_by_user of this DataFileVersionInfo.  # noqa: E501


        :return: The submitted_by_user of this DataFileVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by_user

    @submitted_by_user.setter
    def submitted_by_user(self, submitted_by_user):
        """Sets the submitted_by_user of this DataFileVersionInfo.


        :param submitted_by_user: The submitted_by_user of this DataFileVersionInfo.  # noqa: E501
        :type: str
        """

        self._submitted_by_user = submitted_by_user

    @property
    def version_id(self):
        """Gets the version_id of this DataFileVersionInfo.  # noqa: E501


        :return: The version_id of this DataFileVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this DataFileVersionInfo.


        :param version_id: The version_id of this DataFileVersionInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

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
        if issubclass(DataFileVersionInfo, dict):
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
        if not isinstance(other, DataFileVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
