import os
import tempfile
import pytest
from src.config import create_glitter_dir, create_glitter_config
import json

@pytest.fixture(autouse=False)
def setup_glitter_directory(monkeypatch_dirs):
    create_glitter_dir()
    create_glitter_config()

@pytest.fixture(autouse=True)
def monkeypatch_dirs(monkeypatch):
    temp_dir = tempfile.TemporaryDirectory()

    monkeypatch.setattr("src.config.home_dir", temp_dir.name)
    glitter_dir_path = os.path.join(temp_dir.name, ".glitter")
    monkeypatch.setattr("src.config.glitter_dir", glitter_dir_path)
    monkeypatch.setattr("src.config.glitter_config_file_path", os.path.join(glitter_dir_path, "glitter_config.json"))
    monkeypatch.setattr("src.config.cache_dir", os.path.join(glitter_dir_path, ".glitter_cache"))

    yield temp_dir
