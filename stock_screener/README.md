# Stock screener

In this project there is a python script which takes in a dataframe of stock market symbols, downloads the latest financial data using the yfinance library, and writes it to a csv file. We will do exploratory data analysis on the resultant dataframe, and use value investing principles inspired by prof. Damodaran's NYU course and Joel Greenblatt's *The Little Book That Beats the Market* as guides to filter down the most undervalued companies by sector.

Common investing wisdom says a Price to Earnings ratio lower than 14 means that the company is undervalued. We reject this assumption on the basis that it's too general. What we do instead in the jupyter notebook is checking the actual medians for each sector, and then using those quantiles to screen (filter down) our dataset to get the companies that seem to be most undervalued. The metrics we will use are traling P/E, EV/EBITDA, Return on Assets, and Return on Equity. We look for companies with low value, but high returns. For this to be efficient we need financial data on at least 500-1000 companies.

While there's absolutely no guarantee that the stocks we get as output will be good picks, it gives us a good start for less quantitative exploration like moat, checking the competitors, research on management, reading  news about the industry. It also might be good idea to do a discount cash flow analysis on our top picks. But we set all this aside for now.

This gives us a snapshot of the stock market. During less volatile times, it's probably enough to screen once every financial quarter. However after stock market corrections and "black swan" events it's probably wiser to run the screen a bit more often.

For educational purposes only, not financial advice.

## Few caveats:

- We presume that all companies with no trailing PE are overpriced
- For financial companies, a more useful metric would be Price to Book ratio. There's a short screen on this at the end of the notebook.
- For young growth companies Enterprise to Revenue might be a good metric
- Airlines: because of the lockdowns most airlines are in financial trouble, or at least have negative earnings. For these P/B, EV/Revenue  and current ratio might be good metrics.
- Semiconductors: the chip shortage caused the revenues skyrocket in this sector. It depends on the interpreter whether they think these earnings are sustainable.
- Oil: oil prices have been very high in the past few months, and because of this oil companies make a lot of money, so they operate with higher margins than usual. It remains to be seen whether these oil prices are sustainable in the global economy going forward.
