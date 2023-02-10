from func import *


operations_by_date = []
operation_list = operations()
executed_operations = []

for i in range(len(operation_list)):
    """Фильтруем список операций по параметру "исполнено", т.е. убираем отклоненные операции"""
    if "state" not in operation_list[i]:
        continue
    if operation_list[i]["state"] == "EXECUTED":
        executed_operations.append(operation_list[i]['date'])

"""Сортируем полученный список исполненных операций по дате"""
sorted_list = sorted(executed_operations, reverse=True)
index = 0

while index < 5:
    """Выводим 5 последних операций клиента в требуемом формате"""
    for i in range(len(operation_list)):
        if 'date' not in operation_list[i]:
            continue
        if operation_list[i]['date'] == sorted_list[index]:
            date = operation_list[i]['date']
            description = operation_list[i]['description']
            send_from = operation_list[i]['from']
            send_to = operation_list[i]['to']
            amount = operation_list[i]['operationAmount']['amount']
            currency = operation_list[i]['operationAmount']['currency']['name']
            print(f' {reformat_date(date)} {description}\n '
                  f'{reformat_card_name(send_from)} {reformat_card_number(send_from)} -> '
                  f'{reformat_invoice_name(send_to)} {reformat_invoice(send_to)}\n {amount} {currency}\n')
    index += 1