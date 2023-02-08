import json
import datetime


def operations():
    """Открываем файл и приводим его к формату python"""
    with open ('operations.json', encoding='utf-8') as file:
        raw_json = file.read()
        corrected_list = json.loads(raw_json)
        return corrected_list


def reformat_date(date):
    """Преобразуем дату в требуемый формат"""
    format_data = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return f'{format_data.day}-{format_data.month}-{format_data.year}'


def reformat_card_number(send_from):
    """Преобразуем номер карты в требуемый формат"""
    card_number_by_element = []
    for i in send_from:
        if i.isdigit():
            card_number_by_element.append(i)
    card_number = str("".join(card_number_by_element))
    lenght_of_stars = len(card_number) - 10
    edit_number_1 = card_number[:6] + lenght_of_stars * "*"
    edit_number_2 = card_number[-4:]
    edit_number = edit_number_1 + edit_number_2
    final_card_number = edit_number[:4] + " " + edit_number[4:8] + " " + edit_number[8:12] + " " + edit_number_2
    return final_card_number

def reformat_card_name(send_from):
    """Преобразуем название карты или счета в графе счет отправителя"""
    card_name_by_element = []
    for i in send_from:
        if not i.isdigit():
            card_name_by_element.append(i)
    card_name = str("".join(card_name_by_element))
    return card_name


def reformat_invoice(send_to):
    """Преобразуем номер счета в требуемый формат"""
    invoice_number_by_element = []
    for i in send_to:
        if i.isdigit():
            invoice_number_by_element.append(i)
    invoice_number = str("".join(invoice_number_by_element))
    reformat_invoice_number = "**" + invoice_number[-4:]
    return reformat_invoice_number


def reformat_invoice_name(send_to):
    """Преобразуем название карты или счета в графе счет получателя"""
    invoice_name_by_element = []
    for i in send_to:
        if not i.isdigit():
            invoice_name_by_element.append(i)
    invoice_name = str("".join(invoice_name_by_element))
    return invoice_name











