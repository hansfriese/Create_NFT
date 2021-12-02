from types import SimpleNamespace
from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible, network, config

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy(
        {"from": account}, publish_source=config["networks"][network.show_active()].get("verify", False))
    tx = simple_collectible.createCollectible(
        breed_to_image_uri["PUG"], {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your PUG at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")

    token_id = simple_collectible.tokenCounter() - 1
    tx = simple_collectible.setTokenURI(
        token_id, breed_to_image_uri["SHIBA_INU"])
    tx.wait(1)
    print(f"The URI of dog image was updated to Shiba Inu!")

    return simple_collectible


def create_new_one():
    simple_collectible = SimpleCollectible[-1]
    account = get_account()

    print(f"Current tokenCounter={simple_collectible.tokenCounter()}")

    tx = simple_collectible.createCollectible(
        breed_to_image_uri["ST_BERNARD"], {"from": account})
    tx.wait(1)

    tokenCounter = simple_collectible.tokenCounter()
    print(
        f"Create new nft for ST_Bernard! tokenCounter={tokenCounter} address={OPENSEA_URL.format(simple_collectible.address, tokenCounter - 1)}")


def main():
    deploy_and_create()
    # create_new_one()
