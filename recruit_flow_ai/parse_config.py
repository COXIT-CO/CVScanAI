from pydantic import BaseModel, Field
from typing import Dict
import os
import json


class Prompts(BaseModel):
    system: str

class ConfigModel(BaseModel):
    model: str
    temperature: float = Field(default=0, ge=0, le=1)
    prompts: Dict[str, Prompts]


def parse_config(config_file):
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file '{config_file}' not found.")

    with open(config_file, 'r', encoding='utf-8') as f:
        config_data = f.read()

    config_json = json.loads(config_data)
    config = ConfigModel.model_validate(config_json)
    return config
