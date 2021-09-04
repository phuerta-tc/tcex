"""Owner Role TQL Filter"""
# standard library
from enum import Enum

# first-party
from tcex.api.tc.v3.api_endpoints import ApiEndpoints
from tcex.api.tc.v3.case_management.filter_abc import FilterABC
from tcex.api.tc.v3.case_management.tql import TQL


class OwnerRoleFilter(FilterABC):
    """Filter Object for OwnerRoles"""

    @property
    def _api_endpoint(self) -> str:
        """Return the API endpoint."""
        return ApiEndpoints.OWNER_ROLES.value

    def available(self, operator: Enum, available: bool) -> None:
        """Filter Available based on **available** keyword.

        Args:
            operator: The operator enum for the filter.
            available: The availability status of the role.
        """
        self._tql.add_filter('available', operator, available, TQL.Type.BOOLEAN)

    def comm_role(self, operator: Enum, comm_role: bool) -> None:
        """Filter Community Role based on **commRole** keyword.

        Args:
            operator: The operator enum for the filter.
            comm_role: The scope of the role.
        """
        self._tql.add_filter('commRole', operator, comm_role, TQL.Type.BOOLEAN)

    def description_admin(self, operator: Enum, description_admin: str) -> None:
        """Filter Admin Description based on **descriptionAdmin** keyword.

        Args:
            operator: The operator enum for the filter.
            description_admin: The description of this role's admin access.
        """
        self._tql.add_filter('descriptionAdmin', operator, description_admin, TQL.Type.STRING)

    def description_comm(self, operator: Enum, description_comm: str) -> None:
        """Filter Community Description based on **descriptionComm** keyword.

        Args:
            operator: The operator enum for the filter.
            description_comm: The description of this role's access within a community.
        """
        self._tql.add_filter('descriptionComm', operator, description_comm, TQL.Type.STRING)

    def description_org(self, operator: Enum, description_org: str) -> None:
        """Filter Organization Description based on **descriptionOrg** keyword.

        Args:
            operator: The operator enum for the filter.
            description_org: The description of this role's access within an organization.
        """
        self._tql.add_filter('descriptionOrg', operator, description_org, TQL.Type.STRING)

    def id(self, operator: Enum, id: int) -> None:  # pylint: disable=redefined-builtin
        """Filter ID based on **id** keyword.

        Args:
            operator: The operator enum for the filter.
            id: The ID of the user.
        """
        self._tql.add_filter('id', operator, id, TQL.Type.INTEGER)

    def name(self, operator: Enum, name: str) -> None:
        """Filter Name based on **name** keyword.

        Args:
            operator: The operator enum for the filter.
            name: The name of the role.
        """
        self._tql.add_filter('name', operator, name, TQL.Type.STRING)

    def org_role(self, operator: Enum, org_role: bool) -> None:
        """Filter Organization Role based on **orgRole** keyword.

        Args:
            operator: The operator enum for the filter.
            org_role: The scope of this role.
        """
        self._tql.add_filter('orgRole', operator, org_role, TQL.Type.BOOLEAN)

    def version(self, operator: Enum, version: int) -> None:
        """Filter Version based on **version** keyword.

        Args:
            operator: The operator enum for the filter.
            version: The version number of the role.
        """
        self._tql.add_filter('version', operator, version, TQL.Type.INTEGER)
