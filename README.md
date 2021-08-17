# Калькурятор денег и калорий (ООП)

## Два калькулятора: для подсчёта денег и калорий.

Калькулятор денег умеет:

- Сохраняет новую запись о расходах методом `add_record()`
- Считает, сколько денег потрачено сегодня методом `get_today_stats()`
- Определяет, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод `get_today_cash_remained(currency)`
- Считает, сколько денег потрачено за последние 7 дней — метод `get_week_stats()`

Калькулятор калорий умеет:

- Сохраняет новую запись о приёме пищи — метод `add_record()`
- Считает, сколько калорий уже съедено сегодня — `метод get_today_stats()`
- Определяет, сколько ещё калорий можно/нужно получить сегодня — метод `get_calories_remained()`
- Считает, сколько калорий получено за последние 7 дней — метод `get_week_stats()`
