"""Workflow Template TQL Filter"""
# standard library
from enum import Enum

# first-party
from tcex.api.tc.v3.api_endpoints import ApiEndpoints
from tcex.api.tc.v3.case_management.filter_abc import FilterABC
from tcex.api.tc.v3.case_management.tql import TQL


class WorkflowTemplateFilter(FilterABC):
    """Filter Object for WorkflowTemplates"""

    @property
    def _api_endpoint(self) -> str:
        """Return the API endpoint."""
        return ApiEndpoints.WORKFLOW_TEMPLATES.value

    def active(self, operator: Enum, active: bool) -> None:
        """Filter Active based on **active** keyword.

        Args:
            operator: The operator enum for the filter.
            active: The active status of this template.
        """
        self._tql.add_filter('active', operator, active, TQL.Type.BOOLEAN)

    def description(self, operator: Enum, description: str) -> None:
        """Filter Description based on **description** keyword.

        Args:
            operator: The operator enum for the filter.
            description: The description of this template.
        """
        self._tql.add_filter('description', operator, description, TQL.Type.STRING)

    def id(self, operator: Enum, id: int) -> None:  # pylint: disable=redefined-builtin
        """Filter ID based on **id** keyword.

        Args:
            operator: The operator enum for the filter.
            id: The ID of the template.
        """
        self._tql.add_filter('id', operator, id, TQL.Type.INTEGER)

    def name(self, operator: Enum, name: str) -> None:
        """Filter Name based on **name** keyword.

        Args:
            operator: The operator enum for the filter.
            name: The name of this template.
        """
        self._tql.add_filter('name', operator, name, TQL.Type.STRING)

    def target_id(self, operator: Enum, target_id: int) -> None:
        """Filter Target ID based on **targetId** keyword.

        Args:
            operator: The operator enum for the filter.
            target_id: The assigned user or group ID for the template.
        """
        self._tql.add_filter('targetId', operator, target_id, TQL.Type.INTEGER)

    def target_type(self, operator: Enum, target_type: str) -> None:
        """Filter Target Type based on **targetType** keyword.

        Args:
            operator: The operator enum for the filter.
            target_type: The target type for this template (either User or Group).
        """
        self._tql.add_filter('targetType', operator, target_type, TQL.Type.STRING)

    def version(self, operator: Enum, version: int) -> None:
        """Filter Version based on **version** keyword.

        Args:
            operator: The operator enum for the filter.
            version: The version of this template.
        """
        self._tql.add_filter('version', operator, version, TQL.Type.INTEGER)
