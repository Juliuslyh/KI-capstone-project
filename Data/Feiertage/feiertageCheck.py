from datetime import datetime, date, timedelta
from calendra.europe import Germany
import calendar
import pandas as pd

class feiertag:
    def __init__(self):
        self.Period = [2015, 2016, 2017, 2018, 2019, 2020]

    def load_data(self):
        Period = self.Period

        cal = Germany()
        #print(cal.holidays(2020))
        #print(cal.is_working_day(date(2020, 1, 30)))


        def get_month_range(year, month):
            start_date = date(year, month, 1)
            _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
            end_date = start_date + timedelta(days=days_in_month)
            return (start_date, end_date)

        date_list = []
        holiday_list = []
        date_list_month = []
        holiday_list_month = []

        a_day = timedelta(days=1)
        for year in Period:
            for month in range(1, 13):
                num = 0
                first_day, last_day = get_month_range(year, month)
                while first_day < last_day:
                    date_list.append(first_day)
                    holiday_list.append(cal.is_working_day(first_day))
                    if not cal.is_working_day(first_day):
                        num = num + 1
                    first_day += a_day

                date_list_month.append(date(year,month,1).strftime('%Y-%m'))
                holiday_list_month.append(num)

        df_date = pd.DataFrame(holiday_list, index=date_list)
        df_date.columns = ['is_working_day?']
        df_date.to_csv('date_holiday.csv')

        df_date_monthly = pd.DataFrame(holiday_list_month, index=date_list_month)
        df_date_monthly.columns = ['num of Non-working day']
        df_date_monthly.to_csv('date_holiday_monthly.csv')

if __name__ == '__main__':
    feiertag().load_data()