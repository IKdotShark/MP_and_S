# MP-S (Moduling procceses and systems)
## Входные сигналы
* `Card` - данные карты 💳
* `Bank_confirm` - подтверждение банка ✔
* `Bank_denied` - отрицательный ответ банка ⛔️
## Выходные сигналы:
* `Sender` - отправлен запрос в банк 🔁
* `Valid_Card` - карта хорошая 🙂
* `Invalid_card` - карта вообще не очень ☹️
* `Payment_accepted` - платеж выполнен ✔
* `Payment_denied` - платеж не выполнен ❌
* `Valid_Card_and_Sender` -Sender & Valid_Card
* `Invalid_Card_and_Sender` - Sender & Invalid_Card
## Состояния
* `Card_check` - Проверка карты  💳
* `Bank_answ` - Ответ банка 🏛️
* `Chek_payment` -Проверка наличия средств 💵
## Таблица переходов

|              | Card_check | Bank_answ    | Chek_payment |
| ------------ | ---------- | ------------ | ------------ |
| Card         | Bank_answ  | Bank_answ    | Chek_payment |
| Bank_confirm | Card_check | Chek_payment | Card_check   |
| Bank_denied  | Card_check | Card_check   | Card_check   |
## Таблица входов-выходов

|              | Card_check | Bank_answ              | Chek_payment     |
| ------------ | ---------- | ---------------------- | ---------------- |
| Card         | Sender     | -                      | -                |
| Bank_confirm | -          | Sender \| Valid_Card   | Payment_accepted |
| Bank_denied  | -          | Sender \| Invalid_Card | Payment_denied   |

