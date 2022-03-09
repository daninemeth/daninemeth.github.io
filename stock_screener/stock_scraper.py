from datetime import date
import pandas as pd
import yfinance as yf

#input is a list of stock market tickers (symbols), format needs to be csv and it needs a Symbol column

input_file = input("Please type in the filename: ")
tickers = pd.read_csv(input_file)

#how many stocks do we want? we will pick the n largest by market cap

try:
    n = input('How many tickers would you like to analyze? (n largest by market cap) ')
    n = int(n)
    tickers = tickers.nlargest(n, 'Market Cap')
except:
    n = len(tickers)
    print("Invalid input or no market cap data. We will use the length of the dataframe instead.")

#this will be our output dataframe
df = pd.DataFrame(columns=['Ticker', 'Latest_price', 'sector', 'industry', 'marketCap', 'trailing_PE_ratio', 'pegRatio', 
                                    'enterpriseValue', 'ebitda', 'ebitdaMargins', 'profitMargins', 'revenueGrowth', 'freeCashflow',
                                    'operatingCashflow', 'returnOnAssets', 'returnOnEquity', 'enterpriseToRevenue', 'enterpriseToEbitda',
                                    'priceToBook', 'beta', 'forwardEps', 'currentRatio', 'quickRatio', 'debtToEquity','sharesOutstanding',
                                    'earningsGrowth', 'fiveYearAvgDividendYield'])


filename = f"{input_file[:-4]}_{date.today()}.csv" # we need the date outside the for-loop, because midnight can cause problems

df.to_csv(f"data/{filename}", index=False)
i = 0 #a counter to show how far we have progressed

#looping through the ticker list and downloading data from yahoo finance, appending every row to the csv
for ticker in tickers['Symbol']:

    ticker = yf.Ticker(ticker)
    new_row = pd.DataFrame().reindex_like(df) 

    try:
        new_row.loc[len(new_row)] = {'Ticker': ticker.info['symbol'],
                        'Latest_price': ticker.info['currentPrice'],
                        'sector': ticker.info['sector'],
                        'industry': ticker.info['industry'],
                        'marketCap': ticker.info['marketCap'],
                        'trailing_PE_ratio': ticker.info['trailingPE'],
                        'pegRatio': ticker.info['pegRatio'],
                        'enterpriseValue': ticker.info['enterpriseValue'],
                        'ebitda': ticker.info['ebitda'],
                        'ebitdaMargins': ticker.info['ebitdaMargins'],
                        'profitMargins': ticker.info['profitMargins'],
                        'revenueGrowth': ticker.info['revenueGrowth'],
                        'operatingCashflow': ticker.info['operatingCashflow'],
                        'freeCashflow': ticker.info['freeCashflow'],
                        'returnOnAssets': ticker.info['returnOnAssets'],
                        'returnOnEquity': ticker.info['returnOnEquity'],
                        'enterpriseToRevenue': ticker.info['enterpriseToRevenue'],
                        'enterpriseToEbitda': ticker.info['enterpriseToEbitda'],
                        'priceToBook': ticker.info['priceToBook'],
                        'beta': ticker.info['beta'],
                        'forwardEps': ticker.info['forwardEps'],
                        'currentRatio': ticker.info['currentRatio'],
                        'quickRatio': ticker.info['quickRatio'],
                        'debtToEquity': ticker.info['debtToEquity'],
                        'sharesOutstanding': ticker.info['sharesOutstanding'],
                        'earningsGrowth': ticker.info['earningsGrowth'],
                        'fiveYearAvgDividendYield': ticker.info['fiveYearAvgDividendYield']}
        

        new_row.to_csv(f"data/{filename}", header=False, index=False, mode='a')
             
    
    except Exception as e:
        print(f"{e} for {ticker}")
        try:                                  
                #for some reason only trailingPE breaks the loop if it's missing, everything else is Nan

            new_row.loc[len(new_row)] = {'Ticker': ticker.info['symbol'],
                        'Latest_price': ticker.info['currentPrice'],
                        'sector': ticker.info['sector'],
                        'industry': ticker.info['industry'],
                        'marketCap': ticker.info['marketCap'],
                        'pegRatio': ticker.info['pegRatio'],
                        'enterpriseValue': ticker.info['enterpriseValue'],
                        'ebitda': ticker.info['ebitda'],
                        'ebitdaMargins': ticker.info['ebitdaMargins'],
                        'profitMargins': ticker.info['profitMargins'],
                        'revenueGrowth': ticker.info['revenueGrowth'],
                        'operatingCashflow': ticker.info['operatingCashflow'],
                        'freeCashflow': ticker.info['freeCashflow'],
                        'returnOnAssets': ticker.info['returnOnAssets'],
                        'returnOnEquity': ticker.info['returnOnEquity'],
                        'enterpriseToRevenue': ticker.info['enterpriseToRevenue'],
                        'enterpriseToEbitda': ticker.info['enterpriseToEbitda'],
                        'priceToBook': ticker.info['priceToBook'],
                        'beta': ticker.info['beta'],
                        'forwardEps': ticker.info['forwardEps'],
                        'currentRatio': ticker.info['currentRatio'],
                        'quickRatio': ticker.info['quickRatio'],
                        'debtToEquity': ticker.info['debtToEquity'],
                        'sharesOutstanding': ticker.info['sharesOutstanding'],
                        'earningsGrowth': ticker.info['earningsGrowth'],
                        'fiveYearAvgDividendYield': ticker.info['fiveYearAvgDividendYield']}
        

                
                
            new_row.to_csv(f"data/{filename}", header=False, index=False, mode='a')
            
        except:
            pass

    i+=1
    print("In progress...", i, "/", n)
    
