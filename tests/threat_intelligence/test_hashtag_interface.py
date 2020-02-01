# -*- coding: utf-8 -*-
"""Test the TcEx Threat Intel Module."""
import os
from random import randint

from .ti_helpers import TIHelper, TestThreatIntelligence


class TestHashTagIndicators(TestThreatIntelligence):
    """Test TcEx Hash Tag Indicators."""

    indicator_field = 'Hashtag'
    indicator_field_arg = indicator_field.replace(' ', '_').lower()
    indicator_field_custom = 'value1'
    indicator_type = 'Hashtag'
    owner = os.getenv('TC_OWNER')
    ti = None
    ti_helper = None
    tcex = None

    def setup_method(self):
        """Configure setup before all tests."""
        self.ti_helper = TIHelper(self.indicator_type, self.indicator_field_arg)
        self.ti = self.ti_helper.ti
        self.tcex = self.ti_helper.tcex

    def teardown_method(self):
        """Configure teardown before all tests."""
        if os.getenv('TEARDOWN_METHOD') is None:
            self.ti_helper.cleanup()

    def tests_ti_hashtag_create(self):
        """Create an address indicator using specific interface."""
        indicator_data = {
            self.indicator_field_custom: self.ti_helper.rand_hashtag(),
            'confidence': randint(0, 100),
            'owner': self.owner,
            'rating': randint(0, 5),
        }
        ti = self.ti.hashtag(**indicator_data)
        r = ti.create()

        # assert response
        assert r.status_code == 201

        # retrieve indicator for asserts
        ti = self.ti.hashtag(**indicator_data)
        r = ti.single()
        response_data = r.json()
        ti_data = response_data.get('data', {}).get(ti.api_entity)

        # validate response data
        assert r.status_code == 200
        assert response_data.get('status') == 'Success'

        # validate ti data
        assert ti_data.get('confidence') == indicator_data.get('confidence')
        assert ti_data.get(ti.api_entity) == indicator_data.get(ti.api_entity)
        assert ti_data.get('rating') == indicator_data.get('rating')

        # cleanup indicator
        r = ti.delete()
        assert r.status_code == 200

    def tests_ti_hashtag_add_attribute(self, request):
        """Test indicator add attribute."""
        super().indicator_add_attribute(request)

    def tests_ti_hashtag_add_label(self):
        """Test indicator add label."""
        super().indicator_add_label()

    def tests_ti_hashtag_add_tag(self, request):
        """Test indicator delete."""
        super().indicator_add_tag(request)

    def tests_ti_hashtag_delete(self):
        """Test indicator delete."""
        super().indicator_delete()

    def tests_ti_hashtag_get(self):
        """Test indicator get with generic indicator method."""
        super().indicator_get()

    def tests_ti_hashtag_get_includes(self, request):
        """Test indicator get with includes."""
        super().indicator_get_includes(request)

    def tests_ti_hashtag_get_attribute(self, request):
        """Test indicator get attribute."""
        super().indicator_get_attribute(request)

    def tests_ti_hashtag_get_label(self):
        """Test indicator get label."""
        super().indicator_get_label()

    def tests_ti_hashtag_get_tag(self, request):
        """Test indicator get tag."""
        super().indicator_get_tag(request)

    def tests_ti_hashtag_update(self):
        """Test updating indicator metadata."""
        super().indicator_update()
