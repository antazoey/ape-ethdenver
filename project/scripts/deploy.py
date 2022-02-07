from ape import project
from ape.cli import get_user_selected_account


def deploy():
    account = get_user_selected_account(
        prompt_message=f"Select an account to deploy the Banana Jam token"
    )
    account.deploy(project.BananaJamToken)


def main():
    deploy()
