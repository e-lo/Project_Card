import os
import json
import yaml

from project_card_validator import validate_project_card_file

import pytest


SPEC_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "spec",
)

EXAMPLE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "examples",
)

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data",)

TEST_OUT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_out",)

if not os.path.exists(TEST_OUT_DIR):
    os.mkdir(TEST_OUT_DIR)


@pytest.mark.validator
def test_example_project_cards():
    ex_card = os.path.join(EXAMPLE_DIR, "simple_roadway_property_change.yml")
    schema_filename = os.path.join(SPEC_DIR, "spec_project_card.json")
    result = validate_project_card_file(ex_card, schema_filename=schema_filename)
