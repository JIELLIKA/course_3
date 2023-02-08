from func import *

"""Выводим 5 последних операций клиента в требуемом формате"""

operations_by_date = []
operation_list = operations()

for i in range(len(operation_list)):
    if 'date' not in operation_list[i]:
        continue
    operations_by_date.append(operation_list[i]['date'])

sorted_list = sorted(operations_by_date, reverse=True)
index = 0

while index < 6:
    for i in range(len(operation_list)):
        if 'date' not in operation_list[i]:
            continue
        if operation_list[i]['date'] == sorted_list[index] and operation_list[i]['state'] == "EXECUTED":
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