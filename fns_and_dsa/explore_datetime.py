from datetime import datetime, date, time, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

display_current_datetime()


def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()

    future_days_user_asks = timedelta(days=future_date)
    future_time = current_date + future_days_user_asks
    formatted_date = future_time.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date}")

if __name__ == "__main__":
    calculate_future_date()