# -*- coding: utf-8 -*-
"""ThreatConnect TI URL"""
from urllib.parse import quote_plus
from ..indicator import Indicator


class URL(Indicator):
    """Unique API calls for URL API Endpoints"""

    def __init__(self, tcex, text, owner=None, **kwargs):
        """Initialize Class Properties.

        Args:
            text (str): The value for this Indicator.
            active (bool, kwargs): If False the indicator is marked "inactive" in TC.
            confidence (str, kwargs): The threat confidence for this Indicator.
            date_added (str, kwargs): The date timestamp the Indicator was created.
            last_modified (str, kwargs): The date timestamp the Indicator was last modified.
            private_flag (bool, kwargs): If True the indicator is marked as private in TC.
            rating (str, kwargs): The threat rating for this Indicator.
            xid (str, kwargs): The external id for this Indicator.
        """
        super().__init__(tcex, 'URL', 'url', 'urls', owner, **kwargs)
        self.unique_id = kwargs.get('unique_id', text)
        self.data['text'] = text or self.unique_id
        if self.unique_id:
            self.unique_id = quote_plus(self.fully_decode_uri(self.unique_id))

    def can_create(self):
        """Return True if address can be created.

        If the text has been provided returns that the URL can be created, otherwise
        returns that the URL cannot be created.
        """
        return not self.data.get('text') is None

    def _set_unique_id(self, json_response):
        """Set the unique_id provided a json response.

        Args:
            json_response:
        """
        self.unique_id = quote_plus(self.fully_decode_uri(json_response.get('text', '')))
