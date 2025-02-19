"""ThreatConnect TI Intrusion Set"""
# standard library
from typing import TYPE_CHECKING

# first-party
from tcex.api.tc.v2.threat_intelligence.mappings.group.group import Group

if TYPE_CHECKING:
    # first-party
    from tcex.api.tc.v2.threat_intelligence.threat_intelligence import ThreatIntelligence


class IntrusionSet(Group):
    """Unique API calls for IntrustionSet API Endpoints

    Args:
        ti (ThreatIntelligence): An instance of the ThreatIntelligence Class.
        name (str, kwargs): [Required for Create] The name for this Group.
        owner (str, kwargs): The name for this Group. Default to default Org when not provided
    """

    def __init__(self, ti: 'ThreatIntelligence', **kwargs):
        """Initialize Class Properties."""
        super().__init__(
            ti,
            sub_type='Intrusion Set',
            api_entity='intrusionSet',
            api_branch='intrusionSets',
            **kwargs
        )
