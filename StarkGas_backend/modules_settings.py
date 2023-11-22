import asyncio

from modules import *


async def swap_avnu(_id, key, type_account):
    """
    Make swap on Avnu
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    avnu = Avnu(_id, key, type_account)
    return await avnu.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_jediswap(_id, key, type_account):
    """
    Make swap on Jediswap
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    jediswap = Jediswap(_id, key, type_account)
    return await jediswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_myswap(_id, key, type_account):
    """
    Make swap on MySwap
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    myswap = MySwap(_id, key, type_account)
    return await myswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_starkswap(_id, key, type_account):
    """
    Make swap on 10kSwap
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    starkswap = StarkSwap(_id, key, type_account)
    return await starkswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_sithswap(_id, key, type_account):
    """
    Make swap on SithSwap
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    sithswap = SithSwap(_id, key, type_account)
    return await sithswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_protoss(_id, key, type_account):
    """
    Make swap on Protoss
    """

    from_token = "ETH"
    to_token = "USDC"

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    protoss = Protoss(_id, key, type_account)
    return await protoss.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def deposit_zklend(_id, key, type_account):
    """
    Make deposit on ZkLend
    """

    use_token = ["ETH"]

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6

    sleep_from = 20
    sleep_to = 120

    make_withdraw = False

    all_amount = True

    min_percent = 10
    max_percent = 50

    zklend = ZkLend(_id, key, type_account)
    return await zklend.deposit(
        use_token, min_amount, max_amount, decimal, sleep_from,
        sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_nostra(_id, key, type_account):
    """
    Make deposit on Nostra
    """

    use_token = ["ETH"]

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6

    sleep_from = 20
    sleep_to = 120

    make_withdraw = True

    all_amount = True

    min_percent = 10
    max_percent = 50

    zklend = Nostra(_id, key, type_account)
    return await zklend.deposit(
        use_token, min_amount, max_amount, decimal, sleep_from,
        sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def withdraw_zklend(_id, key, type_account):
    """
    Make withdraw from ZkLend
    """

    use_token = ["ETH"]

    zklend = ZkLend(_id, key, type_account)
    return await zklend.withdraw_all(use_token)


async def withdraw_nostra(_id, key, type_account):
    """
    Make withdraw from Nostra
    """

    use_token = ["ETH"]

    zklend = Nostra(_id, key, type_account)
    return await zklend.withdraw_all(use_token)


async def enable_collateral_zklend(_id, key, type_account):
    """
    Enable collaterl on ZkLend
    """

    use_token = ["ETH", "DAI", "USDC"]

    zklend = ZkLend(_id, key, type_account)
    return await zklend.enable_collateral(use_token)


async def disable_collateral_zklend(_id, key, type_account):
    """
    Disable collateral on ZkLend
    """

    use_token = ["DAI"]

    zklend = ZkLend(_id, key, type_account)
    return await zklend.disable_collateral(use_token)


async def make_transfer(_id, key, type_account, recipient):
    """
    Transfer ETH
    """

    min_amount = 0.000001
    max_amount = 0.000001
    decimal = 6

    all_amount = False

    min_percent = 5
    max_percent = 10

    transfer = Transfer(_id, key, type_account, recipient)
    return await transfer.transfer_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def mint_starknet_id(_id, key, type_account):
    starknet_id = StarknetId(_id, key, type_account)
    return await starknet_id.mint()


async def send_mail_dmail(_id, key, type_account):
    dmail = Dmail(_id, key, type_account)
    return await dmail.send_mail()


async def create_collection_pyramid(_id, key, type_account):
    pyramid = Pyramid(_id, key, type_account)
    return await pyramid.mint()


async def cancel_order_unframed(_id, key, type_account):
    unframed = Unframed(_id, key, type_account)
    return await unframed.cancel_order()


async def cancel_order_flex(_id, key, type_account):
    flex = Flex(_id, key, type_account)
    return await flex.cancel_order()


async def deploy_token(_id, key, type_account):
    stark_guardians = StarkGuardians(_id, key, type_account)
    return await stark_guardians.deploy_token()

async def mint_gol(_id, key, type_account):
    gol = Gol(_id, key, type_account)
    await gol.mint_token()
    