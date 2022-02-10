
import pytest
import ape

from ape_tokens import tokens


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def some_rando(accounts):
    return accounts[1]


@pytest.fixture
def weth_holder():
    # TODO: Replace with impersonated account.
    return ape.accounts.load("weth_account")


@pytest.fixture
def weth():
    return tokens["WETH"]


@pytest.fixture
def token(owner, project, weth):
    return owner.deploy(project.DownstreamERC20, weth.address)
