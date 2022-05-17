import schedule
import requests


def day_tasks():
    all_tasks = {
        '12:00 :': 'check BTC price',
        '13:30 :': 'Workout'
    }

    print('Start the day')
    for k, v in all_tasks.items():
        print(f'its already {k} , start doing {v}')

    response = requests.get(url='http://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = round(data.get('btc_usd').get('last'), 2)

    print(btc_price)


def main():
    day_tasks()
    schedule.every().day.at('22:51').do(day_tasks)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()
