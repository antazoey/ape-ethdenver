# Ape EthDenver Workshop

This repository is for the Ape Eth Denver workshop 2022.
There are two examples here:

1. A demo project
2. A demo plugin

## Setup python env

Install poetry
```bash
pip3 install poetry
```

Install project
```bash
poetry install
```

Activate venv shell
```bash
poetry shell
```

Install eth-ape (poetry add failes for some dependency conflict)
```bash
pip install eth-ape
```
## Demo Project

The demo project is found in the `project/` directory.
Install the plugins by doing:

```bash
ape plugins install .
```

List your existing plugins by doing:

```bash
ape plugins list
```

After the `solidity` plugin is installed, compile the project:

```bash
ape compile
```

Try running the tests:

## Deploy Contract

Setup environment variable `WEB3_ALCHEMY_API_KEY`
```bash
export WEB3_ALCHEMY_API_KEY=<someKey>
```

generate test account
```bash
ape accounts test
```

Install token list
```bash
ape tokens install tokens.1inch.eth
```


## Demo Plugin

The demo plugin is found in the `plugin/` directory. NOTE: This is not a real plugin (yet).

The demo plugin is an example of a `ProviderAPI` implementation for [Chainstack](https://chainstack.com/).
It is similar to plugins [ape-infura](https://github.com/ApeWorX/ape-infura) or [ape-alchemy](https://github.com/ApeWorX/ape-alchemy).

Install the plugin by doing:

```bash
pip install plugin/
```

Create a Chainstack node, set the environment variable `CHAINSTACK_{NETWORK_NAME}_URL` to your node's URL replacing `{NETWORK_NAME}` with the network you used when creating the node.

Launch a console using Chainstack by doing:

```bash
ape console --network :rinkeby:chainstack
```

Now, you are in an interactive environment while connected to your Chainstack node.
