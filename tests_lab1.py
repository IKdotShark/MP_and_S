import unittest
from lab1 import *

class TestPaymentSystem(unittest.TestCase):

    def test_card_check_luhn_algorithm(self):
        # Проверка правильной карты
        self.assertEqual(card_check("4532015112830366", "12/24", "123"), True)
        # Неправильная карта по алгоритму Луна
        self.assertEqual(card_check("4532015112830367", "12/24", "123"), "Номер карты недействителен по алгоритму Луна.")

    def test_card_check_expiry_date(self):
        # Проверка карты с истекшим сроком действия
        self.assertEqual(card_check("4532015112830366", "12/22", "123"), "Срок действия карты недействителен.")
        # Проверка карты с допустимым сроком действия
        self.assertEqual(card_check("4532015112830366", "12/25", "123"), True)

    def test_card_check_cvc(self):
        # Неправильный CVC-код
        self.assertEqual(card_check("4532015112830366", "12/24", "12"), "CVC/CVV код недействителен.")
        # Правильный CVC-код
        self.assertEqual(card_check("4532015112830366", "12/24", "123"), True)

    def test_bank_answer(self):
        # Ответ банка "Yes"
        self.assertEqual(bank_answer("Yes"), True)
        # Ответ банка "No"
        self.assertEqual(bank_answer("No"), "Отрицательный ответ банка")
        # Неверный ответ
        self.assertEqual(bank_answer("Maybe"), "Неверный ответ банка")

    def test_payment_check(self):
        # Успешная покупка
        self.assertEqual(payment_check(100, 50, "Yes"), True)
        # Недостаточно средств на карте
        self.assertEqual(payment_check(50, 100, "Yes"), "Стоимость покупки больше баланса")
        # Отказ от покупки пользователем
        self.assertEqual(payment_check(100, 50, "No"), "Отрицательный ответ пользователя")
        # Неверный ответ пользователя
        self.assertEqual(payment_check(100, 50, "Maybe"), "Неверный ответ пользователя")


if __name__ == '__main__':
    unittest.main()
