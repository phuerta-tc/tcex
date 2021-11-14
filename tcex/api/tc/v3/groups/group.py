"""Group / Groups Object"""
# standard library
from typing import TYPE_CHECKING

# first-party
from tcex.api.tc.v3.api_endpoints import ApiEndpoints
from tcex.api.tc.v3.group_attributes.group_attribute_model import GroupAttributeModel
from tcex.api.tc.v3.groups.group_filter import GroupFilter
from tcex.api.tc.v3.groups.group_model import GroupModel, GroupsModel
from tcex.api.tc.v3.indicators.indicator_model import IndicatorModel
from tcex.api.tc.v3.object_abc import ObjectABC
from tcex.api.tc.v3.object_collection_abc import ObjectCollectionABC
from tcex.api.tc.v3.security_labels.security_label_model import SecurityLabelModel
from tcex.api.tc.v3.tags.tag_model import TagModel

if TYPE_CHECKING:  # pragma: no cover
    # first-party
    from tcex.api.tc.v3.group_attributes.group_attribute import GroupAttribute
    from tcex.api.tc.v3.indicators.indicator import Indicator
    from tcex.api.tc.v3.security_labels.security_label import SecurityLabel
    from tcex.api.tc.v3.tags.tag import Tag


class Groups(ObjectCollectionABC):
    """Groups Collection.

    # Example of params input
    {
        'result_limit': 100,  # Limit the retrieved results.
        'result_start': 10,  # Starting count used for pagination.
        'fields': ['caseId', 'summary']  # Select additional return fields.
    }

    Args:
        session (Session): Session object configured with TC API Auth.
        tql_filters (list): List of TQL filters.
        params (dict): Additional query params (see example above).
    """

    def __init__(self, **kwargs) -> None:
        """Initialize class properties."""
        super().__init__(
            kwargs.pop('session', None), kwargs.pop('tql_filter', None), kwargs.pop('params', None)
        )
        self._model = GroupsModel(**kwargs)
        self.type_ = 'groups'

    def __iter__(self) -> 'Group':
        """Iterate over CM objects."""
        return self.iterate(base_class=Group)

    @property
    def _api_endpoint(self) -> str:
        """Return the type specific API endpoint."""
        return ApiEndpoints.GROUPS.value

    @property
    def filter(self) -> 'GroupFilter':
        """Return the type specific filter object."""
        return GroupFilter(self.tql)


class Group(ObjectABC):
    """Groups Object.

    Args:
        assignments (Assignee, kwargs): A list of assignees and escalatees associated with this
            group (Task specific).
        associated_groups (Groups, kwargs): A list of groups associated with this group.
        associated_indicators (Indicators, kwargs): A list of indicators associated with this group.
        associated_victim_assets (VictimAssets, kwargs): A list of victim assets associated with
            this group.
        attributes (GroupAttributes, kwargs): A list of Attributes corresponding to the Group.
        body (str, kwargs): The email Body.
        due_date (str, kwargs): The date and time that the Task is due.
        escalation_date (str, kwargs): The escalation date and time.
        event_date (str, kwargs): The date and time that the incident or event was first created.
        file_name (str, kwargs): The document or signature file name.
        file_text (str, kwargs): The signature file text.
        file_type (str, kwargs): The signature file type.
        first_seen (str, kwargs): The date and time that the campaign was first created.
        from_ (str, kwargs): The email From field.
        header (str, kwargs): The email Header field.
        malware (bool, kwargs): Is the document malware?
        name (str, kwargs): The name of the group.
        owner_name (str, kwargs): The name of the Organization, Community, or Source that the item
            belongs to.
        password (str, kwargs): The password associated with the document (Required if Malware is
            true).
        publish_date (str, kwargs): The date and time that the report was first created.
        reminder_date (str, kwargs): The reminder date and time.
        security_labels (SecurityLabels, kwargs): A list of Security Labels corresponding to the
            Intel item (NOTE: Setting this parameter will replace any existing tag(s) with
            the one(s) specified).
        status (str, kwargs): The status associated with this document, event, task, or incident
            (read only for task, document, and report).
        subject (str, kwargs): The email Subject section.
        tags (Tags, kwargs): A list of Tags corresponding to the item (NOTE: Setting this parameter
            will replace any existing tag(s) with the one(s) specified).
        to (str, kwargs): The email To field .
        type (str, kwargs): The **type** for the Group.
        xid (str, kwargs): The xid of the item.
    """

    def __init__(self, **kwargs) -> None:
        """Initialize class properties."""
        super().__init__(kwargs.pop('session', None))

        # properties
        self._model = GroupModel(**kwargs)
        self._nested_filter = 'has_group'
        self.type_ = 'Group'

    @property
    def _api_endpoint(self) -> str:
        """Return the type specific API endpoint."""
        return ApiEndpoints.GROUPS.value

    @property
    def as_entity(self) -> dict:
        """Return the entity representation of the object."""
        type_ = self.type_
        if hasattr(self.model, 'type'):
            type_ = self.model.type

        return {'type': type_, 'id': self.model.id, 'value': self.model.summary}

    def add_associated_group(self, **kwargs) -> None:
        """Add group to the object.

        Args:
            attributes (GroupAttributes, kwargs): A list of Attributes corresponding to the Group.
            body (str, kwargs): The email Body.
            due_date (str, kwargs): The date and time that the Task is due.
            escalation_date (str, kwargs): The escalation date and time.
            event_date (str, kwargs): The date and time that the incident or event was first
                created.
            file_name (str, kwargs): The document or signature file name.
            file_text (str, kwargs): The signature file text.
            file_type (str, kwargs): The signature file type.
            first_seen (str, kwargs): The date and time that the campaign was first created.
            from_ (str, kwargs): The email From field.
            header (str, kwargs): The email Header field.
            malware (bool, kwargs): Is the document malware?
            name (str, kwargs): The name of the group.
            owner_name (str, kwargs): The name of the Organization, Community, or Source that the
                item belongs to.
            password (str, kwargs): The password associated with the document (Required if Malware
                is true).
            publish_date (str, kwargs): The date and time that the report was first created.
            reminder_date (str, kwargs): The reminder date and time.
            status (str, kwargs): The status associated with this document, event, task, or incident
                (read only for task, document, and report).
            subject (str, kwargs): The email Subject section.
            to (str, kwargs): The email To field .
            type (str, kwargs): The **type** for the Group.
            xid (str, kwargs): The xid of the item.
        """
        self.model.associated_groups.data.append(GroupModel(**kwargs))

    def add_associated_indicator(self, **kwargs) -> None:
        """Add indicator to the object.

        Args:
            active (bool, kwargs): Is the indicator active?
            active_locked (bool, kwargs): Lock the indicator active value?
            address (str, kwargs): The email address associated with this indicator (EmailAddress
                specific summary field).
            attributes (IndicatorAttributes, kwargs): A list of Attributes corresponding to the
                Indicator.
            confidence (int, kwargs): The indicator threat confidence.
            description (str, kwargs): The indicator description text.
            dns_active (bool, kwargs): Is dns active for the indicator?
            host_name (str, kwargs): The host name of the indicator (Host specific summary field).
            ip (str, kwargs): The ip address associated with this indicator (Address specific
                summary field).
            md5 (str, kwargs): The md5 associated with this indicator (File specific summary field).
            owner_name (str, kwargs): The name of the Organization, Community, or Source that the
                item belongs to.
            private_flag (bool, kwargs): Is this indicator private?
            rating (int, kwargs): The indicator threat rating.
            sha1 (str, kwargs): The sha1 associated with this indicator (File specific summary
                field).
            sha256 (str, kwargs): The sha256 associated with this indicator (File specific summary
                field).
            size (int, kwargs): The size of the file.
            source (str, kwargs): The source for this indicator.
            text (str, kwargs): The url text value of the indicator (Url specific summary field).
            type (str, kwargs): The **type** for the Indicator.
            value1 (str, kwargs): Custom Indicator summary field value1.
            value2 (str, kwargs): Custom Indicator summary field value2.
            value3 (str, kwargs): Custom Indicator summary field value3.
            whois_active (bool, kwargs): Is whois active for the indicator?
        """
        self.model.associated_indicators.data.append(IndicatorModel(**kwargs))

    def add_attribute(self, **kwargs) -> None:
        """Add attribute to the object.

        Args:
            default (bool, kwargs): A flag indicating that this is the default attribute of its type
                within the object. Only applies to certain attribute and data types.
            source (str, kwargs): The attribute source.
            value (str, kwargs): Attribute value.
        """
        self.model.attributes.data.append(GroupAttributeModel(**kwargs))

    def add_security_label(self, **kwargs) -> None:
        """Add security_label to the object.

        Args:
            color (str, kwargs): Color of the security label.
            description (str, kwargs): Description of the security label.
            name (str, kwargs): Name of the security label.
        """
        self.model.security_labels.data.append(SecurityLabelModel(**kwargs))

    def add_tag(self, **kwargs) -> None:
        """Add tag to the object.

        Args:
            description (str, kwargs): A brief description of the Tag.
            name (str, kwargs): The **name** for the Tag.
        """
        self.model.tags.data.append(TagModel(**kwargs))

    @property
    def associated_groups(self) -> 'Group':
        """Yield Group from Groups."""
        yield from self._iterate_over_sublist(Groups)

    @property
    def associated_indicators(self) -> 'Indicator':
        """Yield Indicator from Indicators."""
        # first-party
        from tcex.api.tc.v3.indicators.indicator import Indicators

        yield from self._iterate_over_sublist(Indicators)

    @property
    def attributes(self) -> 'GroupAttribute':
        """Yield Attribute from Attributes."""
        # first-party
        from tcex.api.tc.v3.group_attributes.group_attribute import GroupAttributes

        yield from self._iterate_over_sublist(GroupAttributes)

    @property
    def security_labels(self) -> 'SecurityLabel':
        """Yield Security_Label from Security_Labels."""
        # first-party
        from tcex.api.tc.v3.security_labels.security_label import SecurityLabels

        yield from self._iterate_over_sublist(SecurityLabels)

    @property
    def tags(self) -> 'Tag':
        """Yield Tag from Tags."""
        # first-party
        from tcex.api.tc.v3.tags.tag import Tags

        yield from self._iterate_over_sublist(Tags)
