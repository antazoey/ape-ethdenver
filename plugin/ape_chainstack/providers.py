import keyring
from ape.api import UpstreamProvider, Web3Provider
from web3 import HTTPProvider, Web3
from web3.middleware import geth_poa_middleware


class Chainstack(Web3Provider, UpstreamProvider):
    @property
    def connection_str(self) -> str:
        # Since you specify the network before starting a Chainstack node,
        # we need to get and store URLs based network names.
        network_name = self.network.name
        return keyring.get_password(f"ape-chainstack-{network_name}", "CHAINSTACK_URL")

    def connect(self):
        self._web3 = Web3(HTTPProvider(self.connection_str))
        if self._web3.eth.chain_id in (4, 5, 42):
            self._web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        return super().connect()

    def disconnect(self):
        self._web3 = None
        return super().disconnect()
