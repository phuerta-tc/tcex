"""Testing TcEx Input module field types."""
# standard library
from typing import TYPE_CHECKING, Optional

# third-party
import pytest
from pydantic import BaseModel, ValidationError

# first-party
from tcex.input.field_types import TCEntityArray, TCEntityArrayOptional

from .utils import InputTest

if TYPE_CHECKING:
    from ..mock_app import MockApp


class TestInputsFieldTypeTCEntityArray(InputTest):
    """Test TcEx TCEntityArray and TCEntityArrayOptional Inputs"""

    def test_field_type_entity_array_input_entity_staged(self, playbook_app: 'MockApp'):
        """Test TCEntityArray field type with TCEntity input.

        Input value staged in key value store.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: TCEntityArray

        entity = {'type': 'Address', 'value': '8.8.8.8', 'id': '1000'}
        config_data = {'my_entity': '#App:1234:my_entity!TCEntity'}
        app = playbook_app(config_data=config_data)
        tcex = app.tcex
        self._stage_key_value('my_entity', '#App:1234:my_entity!TCEntity', entity, tcex)
        tcex.inputs.add_model(PytestModel)

        assert tcex.inputs.data.my_entity == [entity]

    def test_field_type_entity_array_input_entity_array_staged(self, playbook_app: 'MockApp'):
        """Test TCEntityArray field type with TCEntity array input.

        Input value staged in key value store.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: TCEntityArray

        entity = [{'type': 'Address', 'value': '8.8.8.8', 'id': '1000'}]
        config_data = {'my_entity': '#App:1234:my_entity!TCEntityArray'}
        app = playbook_app(config_data=config_data)
        tcex = app.tcex
        self._stage_key_value('my_entity', '#App:1234:my_entity!TCEntityArray', entity, tcex)
        tcex.inputs.add_model(PytestModel)

        assert tcex.inputs.data.my_entity == entity

    def test_field_type_entity_array_input_invalid(self, playbook_app: 'MockApp'):
        """Test TCEntityArray field type with non-TCEntity input.

        Exception expected, as values are not TCEntity values (multiple variants tested).
        This test validates both the passing of single invalid values and arrays of
        invalid values.

        Per TCEntityArray.is_array_member, a TCEntity (array member) must be a dictionary that
        contains "type" and "value" keys. The "type" key must be a non-empty string.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        invalid_entity = 'not a tc entity'
        # has no value key
        invalid_entity2 = {'type': 'Address', 'id': '10001'}
        # has no type key
        invalid_entity3 = {'value': '8.8.8.8', 'id': '10001'}
        # type is empty string
        invalid_entity4 = {'type': '', 'value': '8.8.8.8', 'id': '10001'}
        # type is None
        invalid_entity5 = {'type': None, 'value': '8.8.8.8', 'id': '10001'}
        # type is anything else
        invalid_entity6 = {'type': [], 'value': '8.8.8.8', 'id': '10001'}
        # value is not a string (check covers, indicators, groups, etc.)
        invalid_entity7 = {'type': 'Address', 'value': [], 'id': '10001'}
        # Indicator has no id
        invalid_entity8 = {'type': 'Address', 'value': '8.8.8.8'}
        # Indicator id is not string
        invalid_entity9 = {'type': 'Address', 'value': '8.8.8.8', 'id': []}
        # Group has no id
        invalid_entity10 = {'type': 'Adversary', 'value': 'Adversary Name'}
        # Group id is not string
        invalid_entity11 = {'type': 'Adversary', 'value': 'Adversary Name', 'id': []}

        # same scenarios as above, except using array inputs
        invalid_entity12 = ['not a tc entity']
        # has no value key
        invalid_entity13 = [{'type': 'Address', 'id': '10001'}]
        # has no type key
        invalid_entity14 = [{'value': '8.8.8.8', 'id': '10001'}]
        # type is empty string
        invalid_entity15 = [{'type': '', 'value': '8.8.8.8', 'id': '10001'}]
        # type is None
        invalid_entity16 = [{'type': None, 'value': '8.8.8.8', 'id': '10001'}]
        # type is anything else
        invalid_entity17 = [{'type': [], 'value': '8.8.8.8', 'id': '10001'}]
        # value is not a string (check covers, indicators, groups, etc.)
        invalid_entity18 = [{'type': 'Address', 'value': [], 'id': '10001'}]
        # Indicator has no id
        invalid_entity19 = [{'type': 'Address', 'value': '8.8.8.8'}]
        # Indicator id is not string
        invalid_entity20 = [{'type': 'Address', 'value': '8.8.8.8', 'id': []}]
        # Group has no id
        invalid_entity21 = [{'type': 'Adversary', 'value': 'Adversary Name'}]
        # Group id is not string
        invalid_entity22 = [{'type': 'Adversary', 'value': 'Adversary Name', 'id': []}]

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: TCEntityArray
            my_entity2: TCEntityArray
            my_entity3: TCEntityArray
            my_entity4: TCEntityArray
            my_entity5: TCEntityArray
            my_entity6: TCEntityArray
            my_entity7: TCEntityArray
            my_entity8: TCEntityArray
            my_entity9: TCEntityArray
            my_entity10: TCEntityArray
            my_entity11: TCEntityArray
            my_entity12: TCEntityArray
            my_entity13: TCEntityArray
            my_entity14: TCEntityArray
            my_entity15: TCEntityArray
            my_entity16: TCEntityArray
            my_entity17: TCEntityArray
            my_entity18: TCEntityArray
            my_entity19: TCEntityArray
            my_entity20: TCEntityArray
            my_entity21: TCEntityArray
            my_entity22: TCEntityArray

        config_data = {
            'my_entity': invalid_entity,
            'my_entity2': invalid_entity2,
            'my_entity3': invalid_entity3,
            'my_entity4': invalid_entity4,
            'my_entity5': invalid_entity5,
            'my_entity6': invalid_entity6,
            'my_entity7': invalid_entity7,
            'my_entity8': invalid_entity8,
            'my_entity9': invalid_entity9,
            'my_entity10': invalid_entity10,
            'my_entity11': invalid_entity11,
            'my_entity12': invalid_entity12,
            'my_entity13': invalid_entity13,
            'my_entity14': invalid_entity14,
            'my_entity15': invalid_entity15,
            'my_entity16': invalid_entity16,
            'my_entity17': invalid_entity17,
            'my_entity18': invalid_entity18,
            'my_entity19': invalid_entity19,
            'my_entity20': invalid_entity20,
            'my_entity21': invalid_entity21,
            'my_entity22': invalid_entity22,
        }
        app = playbook_app(config_data=config_data)
        tcex = app.tcex

        with pytest.raises(ValidationError) as exc_info:
            tcex.inputs.add_model(PytestModel)

        err_msg = str(exc_info.value)

        # all TCEntityArray definitions in model resulted in error
        assert all(entity in err_msg for entity in config_data.keys())

        # all TCEntityArray definitions resulted in the same error
        assert err_msg.count("not of Array's type") == len(config_data.keys())

    @staticmethod
    def test_field_type_entity_array_input_empty_array(playbook_app: 'MockApp'):
        """Test TCEntityArray field type with empty array input.

        This test is expected to fail, as TCEntityArrayOptional type is not used when
        defining my_entity.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: Optional[TCEntityArray]

        config_data = {'my_entity': []}
        tcex = playbook_app(config_data=config_data).tcex

        with pytest.raises(ValidationError) as exc_info:
            tcex.inputs.add_model(PytestModel)

        assert 'Array must have at least one element' in str(exc_info.value)

    @staticmethod
    def test_field_type_entity_array_optional_input_empty_array(playbook_app: 'MockApp'):
        """Test TCEntityArray field type with empty array input.

        No Exception is expected, as TCEntityArrayOptional type is used

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: Optional[TCEntityArrayOptional]

        config_data = {'my_entity': []}
        tcex = playbook_app(config_data=config_data).tcex
        tcex.inputs.add_model(PytestModel)

        assert tcex.inputs.data.my_entity == []

    def test_field_type_entity_array_input_empty_entity(self, playbook_app: 'MockApp'):
        """Test TCEntityArray field type with empty input.

        Exception expected, as value is empty and TCEntityArrayOptional type is not used.

        Per TCEntityArray.is_empty_member, an empty entity is considered to be a
        dictionary that contains "type" and "value" keys and whose "value" key is an
        empty string. The "type" key must be a non-empty string in order for the
        value to be considered an Entity.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """
        entity = {'type': 'Address', 'value': '', 'id': '1000'}

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            # test for both empty cases
            my_entity: Optional[TCEntityArray]

        config_data = {'my_entity': '#App:1234:my_entity!TCEntity'}
        app = playbook_app(config_data=config_data)
        tcex = app.tcex
        self._stage_key_value('my_entity', '#App:1234:my_entity!TCEntity', entity, tcex)

        with pytest.raises(ValidationError) as exc_info:
            tcex.inputs.add_model(PytestModel)

        err_msg = str(exc_info.value)

        assert 'my_entity' in err_msg
        assert 'may not be empty' in err_msg

    def test_field_type_entity_array_optional_input_empty_entity(self, playbook_app: 'MockApp'):
        """Test TCEntityArray field type with empty input.

        No Exception is expected, as TCEntityArrayOptional type is used.

        Per TCEntityArray.is_empty_member, an empty entity is considered to be a
        dictionary that contains "type" and "value" keys and whose "value" key is an
        empty string. The "type" key must be a non-empty string in order for the
        value to be considered an Entity.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        entity = {'type': 'File', 'value': '', 'id': '1000'}

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            # test for both empty cases
            my_entity: Optional[TCEntityArrayOptional]

        config_data = {
            'my_entity': '#App:1234:my_entity!TCEntity',
        }
        app = playbook_app(config_data=config_data)
        tcex = app.tcex
        self._stage_key_value('my_entity', '#App:1234:my_entity!TCEntity', entity, tcex)
        tcex.inputs.add_model(PytestModel)

        # values coerced to Arrays (list)
        assert tcex.inputs.data.my_entity == [entity]

    @staticmethod
    def test_field_type_entity_array_input_null(playbook_app: 'MockApp'):
        """Test TCEntityArray field type with null input.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: TCEntityArray

        config_data = {'my_entity': None}
        tcex = playbook_app(config_data=config_data).tcex
        with pytest.raises(ValidationError) as exc_info:
            tcex.inputs.add_model(PytestModel)

        assert 'none is not an allowed value' in str(exc_info.value)

    @staticmethod
    def test_field_type_entity_array_optional_input_null(playbook_app: 'MockApp'):
        """Test TCEntityArray field type with null input.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: TCEntityArrayOptional

        config_data = {'my_entity': None}
        tcex = playbook_app(config_data=config_data).tcex
        with pytest.raises(ValidationError) as exc_info:
            tcex.inputs.add_model(PytestModel)

        assert 'none is not an allowed value' in str(exc_info.value)

    @staticmethod
    def test_optional_field_type_entity_array(playbook_app: 'MockApp'):
        """Test TCEntityArray field type with optional input.

        This behavior is expected because Pydantic does not run validators on None input.
        None is allowed due to the wrapping of TCEntityArray with Optional[] typing.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: Optional[TCEntityArray]

        config_data = {'my_entity': None}
        tcex = playbook_app(config_data=config_data).tcex
        tcex.inputs.add_model(PytestModel)

        assert tcex.inputs.data.my_entity is None

    @staticmethod
    def test_optional_field_type_entity_array_optional(playbook_app: 'MockApp'):
        """Test TCEntityArray field type with optional input.

        This behavior is expected because Pydantic does not run validators on None input.
        None is allowed due to the wrapping of TCEntityArrayOptional with Optional[] typing.

        Args:
            playbook_app (fixture): An instance of MockApp.
        """

        class PytestModel(BaseModel):
            """Test Model for Inputs"""

            my_entity: Optional[TCEntityArrayOptional]

        config_data = {'my_entity': None}
        tcex = playbook_app(config_data=config_data).tcex
        tcex.inputs.add_model(PytestModel)

        assert tcex.inputs.data.my_entity is None
