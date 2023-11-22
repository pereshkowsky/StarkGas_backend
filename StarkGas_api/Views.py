import json
from Cors import  App, collectionDataMongo, collectionSettingsMongo, collectionGasMongo

def round_gas(amount):
    if amount.__class__ != float:
        return amount
    return float('{:.5f}'.format(amount))

def round_gas_usd(amount):
    if amount.__class__ != float:
        return amount
    return float('{:.2f}'.format(amount))

# def floor_float(variable: float, precision: int) -> str :
    # if variable.__class__ != float:
    #     return variable
    
    # return float('{:.2f}'.format(variable))
    # part = str(variable).split(".")[0]
    # decimal_part = str(variable).split(".")[1]
    # if len(decimal_part) <= precision:
    #     decimal = decimal_part.ljust(precision, '0')
    #     return part + '.' + decimal
    # else:
    #     return str(round(variable, precision + 1))[:-1]
    # if amount.__class__ != float:
    #     return amount
    # return_amount = ''
    # round_n = 6
    # while True:
    #     return_amount = round(amount, round_n)
    #     if return_amount == 0:
    #         round_n += 1
    #         continue
    #     if return_amount <= 0.01 and round_n == 2:
    #         round_n += 1
    #         continue
    #     break
    # round_n += 1
    # return_amount = round(amount, round_n)
    # return return_amount

# @App.route('/')
# def home():
#     return 'Cors'


@App.route('/API/GAS', methods=['GET'])
def api_gas():
    data_return = []
    data_gas = collectionGasMongo.find()
    for data in data_gas:
        data_return.append(
            {
                'module_name': data.get('module_name'),
                'name': data.get('name'),
                'gwei': data.get('gwei'),
                'gas_status': data.get('gas_status'),
                'gas_time': data.get('gas_time'),
            }
        )
    json_return = json.dumps(data_return)

    return json_return, 200


@App.route('/API/ALL', methods=['GET'])
def api_all():
    data_return = []
    data_starknet_list = []
    data_settings_list = []

    data_settings = collectionSettingsMongo.find({"show_front": "X"})
    data_settings = data_settings.sort({"front_sort": 1})
    for settings in data_settings:
        data_settings_list.append(settings)

    data_starknet = collectionDataMongo.find()
    for data in data_starknet:
        data_starknet_list.append(data)

    for settings in data_settings_list:
        for record in data_starknet_list:
            if record.get('module_name') == settings.get('module_name'):
                data_return.append(
                    {
                        'sort': settings.get('front_sort'),
                        'module_name': record.get('module_name'),
                        'name': record.get('name'),
                        'description': record.get('description'),
                        'with_approve': record.get('with_approve'),
                        'gas_status': record.get('gas_status'),
                        'gas_eth': round_gas(record.get('gas_eth')),
                        'gas_usd': round_gas_usd(record.get('gas_usd')),
                        'url': record.get('url'),
                        'gas_time': record.get('gas_time'),
                    }
                )

    json_return = json.dumps(data_return)

    return json_return, 200