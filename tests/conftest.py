import pytest

from core.config.config_json import ConfigJson
from core.config.config import Config

from activity_entities.activity import Activity
from activity_entities.activity_service import ActivityService

@pytest.fixture
def config():
    yield Config()


@pytest.fixture
def configjson():
    yield ConfigJson()


@pytest.fixture
def activityservice(config):
    yield ActivityService(config)


@pytest.fixture
def activity(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).activity


@pytest.fixture
def type(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).type


@pytest.fixture
def price(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).price


@pytest.fixture
def participants(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).participants


@pytest.fixture
def link(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).link


@pytest.fixture
def key(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).key


@pytest.fixture
def accessibility(configjson) -> str:
    yield Activity.from_response(
        configjson.json
    ).accessibility
