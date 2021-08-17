import datetime as dt


class Record:
    date_format = '%d.%m.%Y'

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.date = date
        self.comment = comment
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date,
                                             self.date_format).date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """Сохраняет новую запись"""
        self.records.append(record)

    def get_today_stats(self):
        """Считает, сколько калорий/денег уже съедено/потрачено сегодня"""
        today = dt.date.today()
        return sum([rec.amount for rec in self.records
                    if rec.date == today])

    def get_week_stats(self):
        """
        Считает, сколько калорий/денег уже
        съедено/потрачено за последние 7 дней
        """
        today = dt.date.today()
        past = today - dt.timedelta(days=7)
        return sum([rec.amount for rec in self.records
                    if past < rec.date <= today])

    def get_today_remain(self):
        """Считает сколько может быть потрачено"""
        result = self.get_today_stats()
        return self.limit - result


class CaloriesCalculator(Calculator):
    """Калькулятор калорий"""
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        """Определяет, сколько ещё калорий можно получить сегодня"""
        may_spend = self.get_today_remain()
        if may_spend > 0:
            return('Сегодня можно съесть что-нибудь ещё, '
                   f'но с общей калорийностью не более {may_spend} кКал')
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    """Калькулятор денег"""
    def __init__(self, limit):
        super().__init__(limit)
    USD_RATE = 70.0
    EURO_RATE = 90.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        """
        Определять, сколько ещё денег можно потратить
        сегодня в рублях, долларах или евро
        """
        may_spend = self.get_today_remain()
        if may_spend == 0:
            return('Денег нет, держись')
        currency_dict = {'rub': (self.RUB_RATE, "руб"),
                         'usd': (self.USD_RATE, "USD"),
                         'eur': (self.EURO_RATE, "Euro")
                         }
        currency_rate, currency_full_name = currency_dict[currency]
        round_may_spend = round(abs(may_spend)/currency_rate, 2)
        if may_spend > 0:
            return (f'На сегодня осталось {round_may_spend} '
                    f'{currency_full_name}')
        else:
            return(f'Денег нет, держись: твой долг - {round_may_spend} '
                   f'{currency_full_name}')


cash_calculator = CashCalculator(2000)
cash_calculator.add_record(Record(amount=45, comment='чай'))
cash_calculator.add_record(Record(amount=350, comment='Маше за обед'))
cash_calculator.add_record(Record(amount=3000,
                                  comment='кушоц суши',
                                  date='11.08.2021'))
print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_today_cash_remained('eur'))
print(f'За прошедшую неделю потрачено {cash_calculator.get_week_stats()} руб')

сalories_calculator = CaloriesCalculator(1500)
сalories_calculator.add_record(Record(amount=400, comment='хинкали'))
сalories_calculator.add_record(Record(amount=500, comment='биргер'))
сalories_calculator.add_record(Record(amount=300,
                                      comment='суши',
                                      date='17.08.2021'))
сalories_calculator.add_record(Record(amount=650,
                                      comment='суши',
                                      date='17.08.2021'))
print(сalories_calculator.get_calories_remained())
