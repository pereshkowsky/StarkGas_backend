from modules_settings import *

A_send_mail_dmail = 'send_mail_dmail'
A_mint_starknet_id = 'mint_starknet_id'
A_swap_avnu = 'swap_avnu'
A_swap_jediswap = 'swap_jediswap'
A_swap_myswap = 'swap_myswap'
A_swap_starkswap = 'swap_starkswap'
A_swap_sithswap = 'swap_sithswap'
A_swap_protoss = 'swap_protoss'
A_deposit_zklend = 'deposit_zklend'
A_deposit_nostra = 'deposit_nostra'
A_withdraw_zklend = 'withdraw_zklend'
A_withdraw_nostra = 'withdraw_nostra'
A_enable_collateral_zklend = 'enable_collateral_zklend'
A_disable_collateral_zklend = 'disable_collateral_zklend'
A_make_transfer = 'make_transfer'
A_cancel_order_unframed = 'cancel_order_unframed'
A_cancel_order_flex = 'cancel_order_flex'


module_info_list = [
    #General
    {
        'module_name':A_make_transfer,
        'name':'Transfer',
        'description':'Other',
        'with_approve':'',
        'module':make_transfer,
        'url':'',
    },
    #Swap
    {
        'module_name':A_swap_avnu,
        'name':'AVNU',
        'description':'DEX',
        'with_approve':'1',
        'module':swap_avnu,
        'url':'https://app.avnu.fi/',
    },
    {
        'module_name':A_swap_jediswap,
        'name':'JediSwap',
        'description':'DEX',
        'with_approve':'1',
        'module':swap_jediswap,
        'url':'https://app.jediswap.xyz/#/swap',
    },
    {
        'module_name':A_swap_myswap,
        'name':'mySwap',
        'description':'DEX',
        'with_approve':'1',
        'module':swap_myswap,
        'url':'https://www.myswap.xyz/#/',
    },
    {
        'module_name':A_swap_starkswap,
        'name':'Starkswap',
        'description':'DEX',
        'with_approve':'1',
        'module':swap_starkswap,
        'url':'https://www.starkswap.co/app/starkswap/swap',
    },
    {
        'module_name':A_swap_sithswap,
        'name':'SithSwap',
        'description':'DEX',
        'with_approve':'1',
        'module':swap_sithswap,
        'url':'https://app.sithswap.com/swap/',
    },
    {
        'module_name':A_swap_protoss,
        'name':'Protoss',
        'description':'DEX',
        'with_approve':'1',
        'module':swap_protoss,
        'url':'https://app.protoss.org/',
    },
    #Other
    {
        'module_name':A_send_mail_dmail,
        'name':'Dmail',
        'description':'DEX',
        'with_approve':'',
        'module':send_mail_dmail,
        'url':'https://mail.dmail.ai/inbox',
    },
    {
        'module_name':A_mint_starknet_id,
        'name':'Starknet ID',
        'description':'Other',
        'with_approve':'',
        'module':mint_starknet_id,
        'url':'https://app.starknet.id/',
    },
    {
        'module_name':A_deposit_zklend,
        'name':'zkLend Deposit',
        'description':'Lending',
        'with_approve':'',
        'module':deposit_zklend,
        'url':'https://app.zklend.com/markets',
    },
    {
        'module_name':A_withdraw_zklend,
        'name':'zkLend Withdraw',
        'description':'Lending',
        'with_approve':'',
        'module':withdraw_zklend,
        'url':'https://app.zklend.com/markets',
    },
    {
        'module_name':A_enable_collateral_zklend,
        'name':'zkLend Collateral ON',
        'description':'Lending',
        'with_approve':'',
        'module':enable_collateral_zklend,
        'url':'https://app.zklend.com/markets',
    },
    {
        'module_name':A_disable_collateral_zklend,
        'name':'zkLend Collateral OFF',
        'description':'Lending',
        'with_approve':'',
        'module':disable_collateral_zklend,
        'url':'https://app.zklend.com/markets',
    },
    {
        'module_name':A_deposit_nostra,
        'name':'Nostra Deposit LP',
        'description':'DEX',
        'with_approve':'',
        'module':deposit_nostra,
        'url':'https://app.nostra.finance/',
    },
    {
        'module_name':A_withdraw_nostra,
        'name':'Nostra Withdraw LP',
        'description':'DEX',
        'with_approve':'',
        'module':withdraw_nostra,
        'url':'https://app.nostra.finance/',
    },
    {
        'module_name':A_mint_gol,
        'name':'Mint Gol',
        'description':'Other',
        'with_approve':'',
        'module':mint_gol,
        'url':'',
    },
    {
        'module_name':A_mint_gol,
        'name':'Mint Gol',
        'description':'Other',
        'with_approve':'',
        'module':mint_gol,
        'url':'',
    },
    {
        'module_name':A_cancel_order_unframed,
        'name':'Unframed Cancel Order',
        'description':'Other',
        'with_approve':'',
        'module':cancel_order_unframed,
        'url':'https://unframed.co/',
    },
    {
        'module_name':A_cancel_order_flex,
        'name':'Flexing Cancel Order',
        'description':'Other',
        'with_approve':'',
        'module':cancel_order_flex,
        'url':'https://flexing.gg/',
    },
]