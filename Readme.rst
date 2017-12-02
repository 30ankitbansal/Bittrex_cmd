Steps to be followed:

1). Create a virtualenv.
    virtualenv --python=python3 bittrex_env

2). Activate the virtualenv.
    source bittrex_env/bin/activate

3). Go to file directory.

4). Run this command.
    pip install --editable .

5). Hist_data:
    hist_data <ccy> <start date> <end date> [-csv] [-all]

    ccy        : Currency pair as: btc-ltc
    start date : yyyy/mm/dd as: 2017/11/01
    end date   : yyyy/mm/dd as: 2017/11/11
    -csv       : optional parameter, return hist_dat.csv containing historical data.
    -all       : optional parameter, return historical data with open and close.

    hist_data btc-ltc 11/01/2017 11/11/2017 [-csv] [-all]

6). pnl:
    pnl <portfolio> [-csv]

    portfolio : pf.csv containing portfolios
    -csv      : return pnl.csv containing currency profit/loss value.

    pnl pf.csv [-csv]

7). update_pf:
    update_pf <orders> [-csv]

    orders : orders.csv containing orders
    -csv   : return update_pf.csv containing updated portfolios