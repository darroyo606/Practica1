import requests


tickers = ["DIS", "KO", "PEP", "INTC", "F", "V"]


def get_price(ticker: str, verbose: bool = False) -> float:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    precio = r['chart']['result'][0]['meta']['regularMarketPrice']
    currency = r['chart']['result'][0]['meta']['currency']

    if verbose:
        print(f"{ticker}: {precio} {currency}")
    return precio


for t in tickers:
    get_price(ticker=t, verbose=True)