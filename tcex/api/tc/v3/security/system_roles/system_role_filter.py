"""System_Role TQL Filter"""
# standard library
from enum import Enum

# first-party
from tcex.api.tc.v3.api_endpoints import ApiEndpoints
from tcex.api.tc.v3.filter_abc import FilterABC
from tcex.api.tc.v3.tql.tql_type import TqlType


class SystemRoleFilter(FilterABC):
    """Filter Object for SystemRoles"""

    @property
    def _api_endpoint(self) -> str:
        """Return the API endpoint."""
        return ApiEndpoints.SYSTEM_ROLES.value

    def active(self, operator: Enum, active: bool) -> None:
        """Filter Active based on **active** keyword.

        Args:
            operator: The operator enum for the filter.
            active: The active status of the role.
        """
        self._tql.add_filter('active', operator, active, TqlType.BOOLEAN)

    def assignable(self, operator: Enum, assignable: bool) -> None:
        """Filter Assignable based on **assignable** keyword.

        Args:
            operator: The operator enum for the filter.
            assignable: The assignable status of the role.
        """
        self._tql.add_filter('assignable', operator, assignable, TqlType.BOOLEAN)

    def displayed(self, operator: Enum, displayed: bool) -> None:
        """Filter Displayed based on **displayed** keyword.

        Args:
            operator: The operator enum for the filter.
            displayed: The displayed status of the role.
        """
        self._tql.add_filter('displayed', operator, displayed, TqlType.BOOLEAN)

    def id(self, operator: Enum, id: int) -> None:  # pylint: disable=redefined-builtin
        """Filter ID based on **id** keyword.

        Args:
            operator: The operator enum for the filter.
            id: The ID of the role.
        """
        self._tql.add_filter('id', operator, id, TqlType.INTEGER)

    def name(self, operator: Enum, name: str) -> None:
        """Filter Name based on **name** keyword.

        Args:
            operator: The operator enum for the filter.
            name: The name of the role.
        """
        self._tql.add_filter('name', operator, name, TqlType.STRING)
