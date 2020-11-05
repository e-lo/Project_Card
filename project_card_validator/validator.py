import os
import json
import logging
import yaml
from jsonschema import validate, ValidationError, SchemaError

DEFAULT_PROJECT_CARD_SCHEMA = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    "spec",
    "spec_project_card.json",
)


def validate_project_card_file(project_card_filename: str, schema_filename: str = DEFAULT_PROJECT_CARD_SCHEMA):
    """
    Validates a project card file based on a schema file. 

    project_card_filename: file location for project card to be validated
    schema_filename: schema location. If not provided, will go to default schema in /spec/spec_project_card.json

    returns: output of ::validate()
    """
    print("Validating {} to {} schema".format(project_card_filename, schema_filename))

    if not os.path.isfile(project_card_filename):
        msg = "{} is not a valid file. Cannot validate.".format(project_card_filename)

    if not os.path.isfile(schema_filename):
        msg = "{} is not a valid file. Cannot validate.".format(schema_filename)

    with open(schema_filename) as schema_json_file:
        schema_dict = json.load(schema_json_file)

        with open(project_card_filename, "r") as card:
            card_json_dict = yaml.safe_load(card)

            return validate_card(card_json_dict, schema_dict)


def validate_card(project_card: dict, schema: dict = {}):
    """
    Validates project card data to a schema definition in json-schema format. 

    project_card: project card as a dict
    schema: schema as a dict

    returns: errors or a report
    """
    
    logging.debug("Validating input:\n {}\n to schema:\n{}\n".format(project_card, schema))

    try:
        validate(project_card, schema)
        return True

    except ValidationError as exc:
        logging.error("Failed Project Card validation: Validation Error")
        logging.error(exc.message)

    except SchemaError as exc:
        logging.error("Failed Project Card schema validation: Schema Error")
        logging.error(exc.message)

    except yaml.YAMLError as exc:
        logging.error(exc.message)
