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

class SystemProjectInfo(object):
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
        'auto_versioning': 'bool',
        'budget': 'float',
        'current_phase': 'str',
        'current_status': 'str',
        'customer': 'str',
        'data_size': 'int',
        'deadline': 'str',
        'end_date': 'str',
        'guid': 'int',
        'has_mass_budget_props': 'bool',
        'is_bkd_template_project': 'bool',
        'is_deleted': 'bool',
        'is_template_project': 'bool',
        'name': 'str',
        'partners': 'str',
        'po_number': 'str',
        'prj_phases': 'list[str]',
        'project_descr': 'str',
        'project_model_id': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'auto_versioning': 'autoVersioning',
        'budget': 'budget',
        'current_phase': 'current_phase',
        'current_status': 'current_status',
        'customer': 'customer',
        'data_size': 'dataSize',
        'deadline': 'deadline',
        'end_date': 'end_date',
        'guid': 'guid',
        'has_mass_budget_props': 'hasMassBudgetProps',
        'is_bkd_template_project': 'is_bkd_template_project',
        'is_deleted': 'is_deleted',
        'is_template_project': 'is_template_project',
        'name': 'name',
        'partners': 'partners',
        'po_number': 'poNumber',
        'prj_phases': 'prjPhases',
        'project_descr': 'project_descr',
        'project_model_id': 'project_model_id',
        'start_date': 'start_date'
    }

    def __init__(self, auto_versioning=None, budget=None, current_phase=None, current_status=None, customer=None, data_size=None, deadline=None, end_date=None, guid=None, has_mass_budget_props=None, is_bkd_template_project=None, is_deleted=None, is_template_project=None, name=None, partners=None, po_number=None, prj_phases=None, project_descr=None, project_model_id=None, start_date=None):  # noqa: E501
        """SystemProjectInfo - a model defined in Swagger"""  # noqa: E501
        self._auto_versioning = None
        self._budget = None
        self._current_phase = None
        self._current_status = None
        self._customer = None
        self._data_size = None
        self._deadline = None
        self._end_date = None
        self._guid = None
        self._has_mass_budget_props = None
        self._is_bkd_template_project = None
        self._is_deleted = None
        self._is_template_project = None
        self._name = None
        self._partners = None
        self._po_number = None
        self._prj_phases = None
        self._project_descr = None
        self._project_model_id = None
        self._start_date = None
        self.discriminator = None
        if auto_versioning is not None:
            self.auto_versioning = auto_versioning
        if budget is not None:
            self.budget = budget
        if current_phase is not None:
            self.current_phase = current_phase
        if current_status is not None:
            self.current_status = current_status
        if customer is not None:
            self.customer = customer
        if data_size is not None:
            self.data_size = data_size
        if deadline is not None:
            self.deadline = deadline
        if end_date is not None:
            self.end_date = end_date
        if guid is not None:
            self.guid = guid
        if has_mass_budget_props is not None:
            self.has_mass_budget_props = has_mass_budget_props
        if is_bkd_template_project is not None:
            self.is_bkd_template_project = is_bkd_template_project
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_template_project is not None:
            self.is_template_project = is_template_project
        if name is not None:
            self.name = name
        if partners is not None:
            self.partners = partners
        if po_number is not None:
            self.po_number = po_number
        if prj_phases is not None:
            self.prj_phases = prj_phases
        if project_descr is not None:
            self.project_descr = project_descr
        if project_model_id is not None:
            self.project_model_id = project_model_id
        if start_date is not None:
            self.start_date = start_date

    @property
    def auto_versioning(self):
        """Gets the auto_versioning of this SystemProjectInfo.  # noqa: E501


        :return: The auto_versioning of this SystemProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._auto_versioning

    @auto_versioning.setter
    def auto_versioning(self, auto_versioning):
        """Sets the auto_versioning of this SystemProjectInfo.


        :param auto_versioning: The auto_versioning of this SystemProjectInfo.  # noqa: E501
        :type: bool
        """

        self._auto_versioning = auto_versioning

    @property
    def budget(self):
        """Gets the budget of this SystemProjectInfo.  # noqa: E501


        :return: The budget of this SystemProjectInfo.  # noqa: E501
        :rtype: float
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this SystemProjectInfo.


        :param budget: The budget of this SystemProjectInfo.  # noqa: E501
        :type: float
        """

        self._budget = budget

    @property
    def current_phase(self):
        """Gets the current_phase of this SystemProjectInfo.  # noqa: E501


        :return: The current_phase of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._current_phase

    @current_phase.setter
    def current_phase(self, current_phase):
        """Sets the current_phase of this SystemProjectInfo.


        :param current_phase: The current_phase of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._current_phase = current_phase

    @property
    def current_status(self):
        """Gets the current_status of this SystemProjectInfo.  # noqa: E501


        :return: The current_status of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._current_status

    @current_status.setter
    def current_status(self, current_status):
        """Sets the current_status of this SystemProjectInfo.


        :param current_status: The current_status of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._current_status = current_status

    @property
    def customer(self):
        """Gets the customer of this SystemProjectInfo.  # noqa: E501


        :return: The customer of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SystemProjectInfo.


        :param customer: The customer of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def data_size(self):
        """Gets the data_size of this SystemProjectInfo.  # noqa: E501


        :return: The data_size of this SystemProjectInfo.  # noqa: E501
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this SystemProjectInfo.


        :param data_size: The data_size of this SystemProjectInfo.  # noqa: E501
        :type: int
        """

        self._data_size = data_size

    @property
    def deadline(self):
        """Gets the deadline of this SystemProjectInfo.  # noqa: E501


        :return: The deadline of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this SystemProjectInfo.


        :param deadline: The deadline of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._deadline = deadline

    @property
    def end_date(self):
        """Gets the end_date of this SystemProjectInfo.  # noqa: E501


        :return: The end_date of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SystemProjectInfo.


        :param end_date: The end_date of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def guid(self):
        """Gets the guid of this SystemProjectInfo.  # noqa: E501


        :return: The guid of this SystemProjectInfo.  # noqa: E501
        :rtype: int
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this SystemProjectInfo.


        :param guid: The guid of this SystemProjectInfo.  # noqa: E501
        :type: int
        """

        self._guid = guid

    @property
    def has_mass_budget_props(self):
        """Gets the has_mass_budget_props of this SystemProjectInfo.  # noqa: E501


        :return: The has_mass_budget_props of this SystemProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_mass_budget_props

    @has_mass_budget_props.setter
    def has_mass_budget_props(self, has_mass_budget_props):
        """Sets the has_mass_budget_props of this SystemProjectInfo.


        :param has_mass_budget_props: The has_mass_budget_props of this SystemProjectInfo.  # noqa: E501
        :type: bool
        """

        self._has_mass_budget_props = has_mass_budget_props

    @property
    def is_bkd_template_project(self):
        """Gets the is_bkd_template_project of this SystemProjectInfo.  # noqa: E501


        :return: The is_bkd_template_project of this SystemProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_bkd_template_project

    @is_bkd_template_project.setter
    def is_bkd_template_project(self, is_bkd_template_project):
        """Sets the is_bkd_template_project of this SystemProjectInfo.


        :param is_bkd_template_project: The is_bkd_template_project of this SystemProjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_bkd_template_project = is_bkd_template_project

    @property
    def is_deleted(self):
        """Gets the is_deleted of this SystemProjectInfo.  # noqa: E501


        :return: The is_deleted of this SystemProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this SystemProjectInfo.


        :param is_deleted: The is_deleted of this SystemProjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_template_project(self):
        """Gets the is_template_project of this SystemProjectInfo.  # noqa: E501


        :return: The is_template_project of this SystemProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_template_project

    @is_template_project.setter
    def is_template_project(self, is_template_project):
        """Sets the is_template_project of this SystemProjectInfo.


        :param is_template_project: The is_template_project of this SystemProjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_template_project = is_template_project

    @property
    def name(self):
        """Gets the name of this SystemProjectInfo.  # noqa: E501


        :return: The name of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemProjectInfo.


        :param name: The name of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def partners(self):
        """Gets the partners of this SystemProjectInfo.  # noqa: E501


        :return: The partners of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._partners

    @partners.setter
    def partners(self, partners):
        """Sets the partners of this SystemProjectInfo.


        :param partners: The partners of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._partners = partners

    @property
    def po_number(self):
        """Gets the po_number of this SystemProjectInfo.  # noqa: E501


        :return: The po_number of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this SystemProjectInfo.


        :param po_number: The po_number of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._po_number = po_number

    @property
    def prj_phases(self):
        """Gets the prj_phases of this SystemProjectInfo.  # noqa: E501


        :return: The prj_phases of this SystemProjectInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._prj_phases

    @prj_phases.setter
    def prj_phases(self, prj_phases):
        """Sets the prj_phases of this SystemProjectInfo.


        :param prj_phases: The prj_phases of this SystemProjectInfo.  # noqa: E501
        :type: list[str]
        """

        self._prj_phases = prj_phases

    @property
    def project_descr(self):
        """Gets the project_descr of this SystemProjectInfo.  # noqa: E501


        :return: The project_descr of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_descr

    @project_descr.setter
    def project_descr(self, project_descr):
        """Sets the project_descr of this SystemProjectInfo.


        :param project_descr: The project_descr of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._project_descr = project_descr

    @property
    def project_model_id(self):
        """Gets the project_model_id of this SystemProjectInfo.  # noqa: E501


        :return: The project_model_id of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_model_id

    @project_model_id.setter
    def project_model_id(self, project_model_id):
        """Sets the project_model_id of this SystemProjectInfo.


        :param project_model_id: The project_model_id of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._project_model_id = project_model_id

    @property
    def start_date(self):
        """Gets the start_date of this SystemProjectInfo.  # noqa: E501


        :return: The start_date of this SystemProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SystemProjectInfo.


        :param start_date: The start_date of this SystemProjectInfo.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(SystemProjectInfo, dict):
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
        if not isinstance(other, SystemProjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other