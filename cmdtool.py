import click
import urllib.request as request
import json
# import csv
# form datetime import datetime as dt
import datetime
import time
import time
import pandas as pd
import os
import bittrex


@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')


obj = bittrex.Bittrex()


@click.command()
@click.option('--all', is_flag=True, help="Will returns also open and close.")
@click.option('--csv', is_flag=True, help="Will returns the data in csv file.")
@click.argument('ccy')
@click.argument('initial_date')
@click.argument('final_date')
def hist_data(csv, all, ccy, initial_date, final_date):
    h_data = obj.hist_data(ccy, initial_date, final_date)
    if all:
        df = pd.DataFrame(h_data, columns=['H', 'L', 'O', 'C', 'T'])
    else:
        df = pd.DataFrame(h_data, columns=['H', 'L', 'T'])
    print(df)

    if csv:
        df.to_csv('hist_data.csv')


@click.command()
@click.option('--csv', is_flag=True, help="Will returns the data in csv file.")
@click.argument('Portfolio', type=click.Path(exists=True))
def pnl(csv, portfolio):
    df = pd.read_csv(portfolio)
    print(df)

    dr = obj.pnl(df)

    if csv:
        # ofile = open('pnl.csv', "w")
        # writer = csv.writer(ofile, delimiter=',')
        dr.to_csv('pnl.csv')
        # writer.writerow(['CCY', 'Quantity', 'Profit/Loss', 'Value'])
        # writer.writerow([ccy, quantity, profit_loss, diff])

        # ofile.close()




@click.command()
@click.option('--csv', is_flag=True, help="Will returns the data in csv file.")
@click.argument('orders', type=click.Path(exists=True))
def update_pf(csv, orders):
    dir = os.path.dirname(os.path.abspath(__file__)) + "/"
    df = pd.read_csv(orders)

    if os.path.exists(dir + 'portfolio.csv'):
        pf_df = pd.read_csv('portfolio.csv')
        pf_df.set_index('OrderUuid')

        pf_df = obj.update_pf(pf_df, df)

        pf_df.to_csv('portfolio.csv', index=False)

    else:
        df.to_csv('portfolio.csv', index=False)

    print(pd.read_csv('portfolio.csv'))

    if csv:
        df = pd.read_csv('portfolio.csv')
        df.to_csv('update_pf.csv')
