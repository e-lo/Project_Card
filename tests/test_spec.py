import os
import json
import pytest

import jsonschema


SPEC_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "spec",
)

TEST_OUT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_out",)

if not os.path.exists(TEST_OUT_DIR):
    os.mkdir(TEST_OUT_DIR)


@pytest.mark.spec
def test_project_card_schema_valid_json():
    schema_filename = os.path.join(SPEC_DIR, "spec_project_card.json")
    with open(schema_filename) as schema_json_file:
        json_object = json.load(schema_json_file)


@pytest.mark.spec
def test_project_card_schema_valid_json_schema():
    schema_filename = os.path.join(SPEC_DIR, "spec_project_card.json")

    default_validator_class = jsonschema.validators.validator_for(schema_filename)

    with open(schema_filename) as schema_json_file:
        default_validator_class.check_schema(json.load(schema_json_file))
