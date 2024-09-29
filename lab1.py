import datetime

import datetime


def validate_card(card_number, expiry_date, cvc):
    # Проверка по алгоритму Луна
    def luhn_algorithm(card_number):
        card_digits = [int(digit) for digit in card_number.replace(" ", "")]
        for i in range(len(card_digits) - 2, -1, -2):
            card_digits[i] *= 2
            if card_digits[i] > 9:
                card_digits[i] -= 9
        return sum(card_digits) % 10 == 0

    # Проверка срока действия карты
    def validate_expiry_date(expiry_date):
        try:
            month, year = map(int, expiry_date.split("/"))
            if not (1 <= month <= 12):
                return False
            current_year = int(str(datetime.datetime.now().year)[-2:])
            current_month = datetime.datetime.now().month
            return (year > current_year) or (year == current_year and month >= current_month)
        except ValueError:
            return False

    # Проверка CVC/CVV кода
    def validate_cvc(cvc):
        return cvc.isdigit() and (len(cvc) == 3 or len(cvc) == 4)

    # Проверка всех условий
    if not luhn_algorithm(card_number):
        return "Номер карты недействителен по алгоритму Луна."

    if not validate_expiry_date(expiry_date):
        return "Срок действия карты недействителен."

    if not validate_cvc(cvc):
        return "CVC/CVV код недействителен."

    return "Все данные карты валидны."


def confirmation_check(card_balance, payment):
    if (card_balance >= payment):
        return True
    else:
        return False


def confirmation_check(payment_confirm):
    if (payment_confirm == "Yes"):
        return True
    else:
        return False


def main():
    card_number = input("Введите номер карты: ")
    expiry_date = input("Введите срок действия карты (ММ/ГГ): ")
    cvc = input("Введите CVC/CVV код: ")
    card_balance = input("Введите баланс карты: ")
    payment = input("Введите стоимость покупки: ")
    payment_check_confirm = input("Подтвердите покупки (Введите Yes/No): ")

    result = validate_card(card_number, expiry_date, cvc)
    print(result)


if __name__ == "__main__":
    main()
