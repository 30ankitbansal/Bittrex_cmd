import urllib.request as request
import json
import datetime
import time
import pandas as pd


class Bittrex:
    def hist_data(self, ccy, initial_date, final_date):
        timestamp = time.mktime(datetime.datetime.strptime(initial_date, '%Y/%m/%d').timetuple())
        ret = request.urlopen(request.Request('https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + ccy +
                                              '&tickInterval=day&_=' + str(timestamp)))
        data = json.loads(ret.read().decode('utf-8'))
        initial_date = time.strptime(initial_date, '%Y/%m/%d')
        final_date = time.strptime(final_date, '%Y/%m/%d')
        h_data = []
        for row in data['result']:
            date = time.strptime(row['T'], '%Y-%m-%dT%H:%M:%S')
            if date > initial_date and date < final_date:
                h_data.append(row)

        return h_data

    def pnl(self, df):
        ret = request.urlopen(request.Request('https://bittrex.com/api/v2.0/pub/currencies/GetBTCPrice'))
        btc_price = json.loads(ret.read().decode('utf-8'))['result']['bpi']['USD']['rate_float']
        result = []
        i = 0
        while i <= df.last_valid_index():
            data = {}
            ccy = df.iloc[i]['ccy']
            quantity = df.iloc[i]['qty']
            reference_price = df.iloc[i]['value']

            ret = request.urlopen(request.Request('https://bittrex.com/api/v1.1/public/getticker?market=' + ccy))
            ccy_btc = json.loads(ret.read().decode('utf-8'))['result']['Last']

            ccy_price = ccy_btc * btc_price

            user_amount = float(quantity) * float(reference_price)
            final_amount = float(quantity) * float(ccy_price)

            diff = final_amount - user_amount

            if user_amount > final_amount:
                profit_loss = 'Loss'
            else:
                profit_loss = 'Profit'
            data['ccy'] = ccy
            data['profit/loss'] = profit_loss
            data['diff'] = diff
            result.append(data)
            i += 1

        dr = pd.DataFrame(result, columns=['ccy', 'profit/loss', 'diff'])
        print(dr)
        return dr

    def update_pf(self, pf_df, df):
        i = 0
        while i <= df.last_valid_index():
            j = 0
            while j <= pf_df.last_valid_index():
                if pf_df.iloc[j]['OrderUuid'] == df.iloc[i]['OrderUuid']:
                    # print('equal found')
                    break
                j += 1
            if j > pf_df.last_valid_index():
                # print('Data to added')
                pf_df.loc[j] = df.loc[i].values

            i += 1
        return pf_df
