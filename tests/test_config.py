import os
import tempfile
import pytest
from src.config import create_glitter_dir, create_glitter_config,update_glitter_config,get_glitter_config
import json
from conftest import monkeypatch_dirs


def test_create_glitter_dir(monkeypatch_dirs):
    temp_dir = monkeypatch_dirs

    expected_glitter_dir = os.path.join(temp_dir.name, ".glitter")
    print(expected_glitter_dir)
    assert not os.path.exists(expected_glitter_dir)

    glitter_dir = create_glitter_dir()

    assert glitter_dir == expected_glitter_dir
    assert os.path.exists(glitter_dir)
    assert os.path.exists(os.path.join(glitter_dir, ".glitter_cache"))


def test_create_glitter_config(monkeypatch_dirs):

    create_glitter_dir()

    temp_dir = monkeypatch_dirs

    expected_config_file_path = os.path.join(temp_dir.name, ".glitter", "glitter_config.json")
    assert not os.path.exists(expected_config_file_path)

    config_file_path = create_glitter_config()

    assert config_file_path == expected_config_file_path
    assert os.path.exists(config_file_path)

    with open(config_file_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    assert config_data == {"projects": {}}


def test_update_and_get_glitter_config(setup_glitter_directory):
    key = "test_key"
    value = "test_value"
    update_glitter_config(key, value)

    config_data = get_glitter_config()

    assert key in config_data
    assert config_data[key] == value


