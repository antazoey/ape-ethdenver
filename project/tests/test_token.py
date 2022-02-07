import pytest


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def receiver(accounts):
    return accounts[1]


@pytest.fixture
def token(owner, project):
    return owner.deploy(project.BananaJamToken)


def test_name(token):
    assert token.name() == "BananaJam"


def test_decimals(token):
    assert token.decimals() == 18


def test_mint(owner, receiver, token):
    token.mint(receiver, 10, sender=owner)
    balance = token.balanceOf(receiver)
    assert balance == 10
