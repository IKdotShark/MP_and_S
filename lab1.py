import datetime
import re

def card_check(card_number, expiry_date, cvc):
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

    return True

def bank_answer(bank_confirm):
    bank_confirm = bank_confirm.lower()
    if re.match(r'^(y(es)?)$', bank_confirm):
        return True
    elif re.match(r'^(n(o)?)$', bank_confirm):
        return "Отрицательный ответ банка"
    else:
        return "Неверный ответ банка"

def payment_check(card_balance, payment, payment_check_confirm):
    if float(card_balance) >= float(payment):
        payment_check_confirm = payment_check_confirm.lower()
        if re.match(r'^(y(es)?)$', payment_check_confirm):
            return True
        elif re.match(r'^(n(o)?)$', payment_check_confirm):
            return "Отрицательный ответ пользователя"
        else:
            return "Неверный ответ пользователя"
    else:
        return "Стоимость покупки больше баланса"

def main():
    cardcheck = card_check()
    if cardcheck:
        bankanswer = bank_answer()
    while not (cardcheck) or not (bankanswer):
        print("")
        cardcheck = card_check()
        if cardcheck:
            bankanswer = bank_answer()
    paymentcheck = payment_check()
    if paymentcheck:
        bankanswer = bank_answer()
    while not (paymentcheck) or not (bankanswer):
        print("")
        paymentcheck = payment_check()
        if paymentcheck:
            bankanswer = bank_answer()
    print("Балдеж")

if __name__ == "__main__":
    main()
