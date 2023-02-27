import requests

in_currency = input()

json_str = requests.get('http://floatrates.com/daily/{currency}.json'.format(currency=in_currency)).json()
if in_currency == 'usd':
    rates = {json_str['eur']['code']: json_str['eur']['rate']}
elif in_currency == 'eur':
    rates = {json_str['usd']['code']: json_str['usd']['rate']}
else:
    rates = {json_str['usd']['code']: json_str['usd']['rate'], json_str['eur']['code']: json_str['eur']['rate']}

while True:
    out_currency = str(input()).upper()
    if out_currency is '':
        break
    amount = float(input())
    print('Checking the cache...')
    if out_currency in rates:
        print('Oh! It is in the cache!')
        output = round(amount * rates[out_currency], 2)
        print(f'You received {output} {out_currency}')
    else:
        print('Sorry, but it is not in the cache!')
        rates[json_str[out_currency.lower()]['code']] = json_str[out_currency.lower()]['rate']
        output = round(amount * rates[out_currency], 2)
        print(f'You received {output} {out_currency}')
