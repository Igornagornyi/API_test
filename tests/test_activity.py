import pytest


@pytest.mark.smoke
def test_check_payload_for_activity(activityservice, activity):
    assert activityservice.from_response_activity() == activity


def test_check_payload_for_activity_len(activityservice):
    assert len(list(activityservice.from_response_activity())) == 30


def test_check_payload_for_type(activityservice, type):
    assert activityservice.from_response_type() == type


def test_check_payload_for_price_type(activityservice):
    assert isinstance(activityservice.from_response_price(), float)


def test_check_payload_for_particioants(activityservice, participants):
    assert activityservice.from_response_participants() == participants


def test_check_payload_for_link(activityservice, link):
    assert activityservice.from_response_link() == link


def test_check_payload_for_key(activityservice, key):
    assert activityservice.from_response_key() == key


def test_check_payload_for_key_type(activityservice):
    assert isinstance(activityservice.from_response_key(), str)


def test_check_payload_for_accessibility(activityservice):
    assert activityservice.from_response_accessibility() < 1

