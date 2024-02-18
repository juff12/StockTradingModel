from polygon import RESTClient
import pandas as pd
from pathlib import Path


sp500_tickers = [
    "MMM", "ABT", "ABBV", "ACN", "ATVI", "ADBE", "AMD", "AES", "AFL", "A",
    "APD", "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL", "GOOGL",
    "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG",
    "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSYS", "ANTM",
    "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG",
    "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR",
    "BLL", "BAC", "BK", "BAX", "BDX", "BRK.B", "BBY", "BIO", "BIIB",
    "BLK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR",
    "BF.B", "CHRW", "COG", "CDNS", "CZR", "CPB", "COF", "CAH", "KMX",
    "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC",
    "CNP", "CERN", "CF", "CRL", "SCHW", "CHTR", "CVX", "CMG", "CB",
    "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CLX",
    "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP",
    "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "COST", "CCI", "CSX",
    "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY",
    "DVN", "DXCM", "FANG", "DLR", "DFS", "DISCA", "DISCK", "DISH", "DG",
    "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DRE", "DD",
    "DXC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR",
    "ENPH", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY",
    "EVRG", "ES", "RE", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV",
    "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC", "FISV",
    "FLT", "FLIR", "FLS", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA",
    "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GNRC", "GD", "GE",
    "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "GWW", "HAL",
    "HBI", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE",
    "HLT", "HFC", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ",
    "HUM", "HBAN", "HII", "IEX", "IDXX", "INFO", "ITW", "ILMN", "INCY",
    "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG",
    "IVZ", "IPGP", "IQV", "IRM", "JKHY", "J", "JBHT", "SJM", "JNJ",
    "JCI", "JPM", "JNPR", "KSU", "K", "KEY", "KEYS", "KMB", "KIM",
    "KMI", "KLAC", "KHC", "KR", "LB", "LHX", "LH", "LRCX", "LW",
    "LVS", "LEG", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV", "LKQ",
    "LMT", "L", "LOW", "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX",
    "MAR", "MMC", "MLM", "MAS", "MA", "MKC", "MXIM", "MCD", "MCK",
    "MDT", "MRK", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA",
    "MHK", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI",
    "MSCI", "NDAQ", "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE",
    "NLSN", "NKE", "NI", "NSC", "NTRS", "NOC", "NLOK", "NCLH", "NOV",
    "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC",
    "OKE", "ORCL", "OTIS", "PCAR", "PKG", "PH", "PAYX", "PAYC", "PYPL",
    "PENN", "PNR", "PBCT", "PEP", "PKI", "PRGO", "PFE", "PM", "PSX",
    "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR",
    "PLD", "PRU", "PTC", "PEG", "PSA", "PHM", "PVH", "QRVO", "PWR",
    "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF",
    "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI",
    "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SPG",
    "SWKS", "SNA", "SO", "LUV", "SWK", "SBUX", "STT", "STE", "SYK",
    "SIVB", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TGT",
    "TEL", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX",
    "TSCO", "TT", "TDG", "TRV", "TFC", "TWTR", "TYL", "TSN", "UDR",
    "ULTA", "USB", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI",
    "UHS", "UNM", "VLO", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VFC",
    "VIAC", "VTRS", "V", "VNT", "VNO", "VMC", "WRB", "WAB", "WMT",
    "WBA", "DIS", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC",
    "WU", "WRK", "WY", "WHR", "WMB", "WLTW", "WYNN", "XEL", "XLNX",
    "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS"
]
nasdaq_100_tickers = [
    "AAPL", "ADBE", "ADI", "ADP", "ADSK", "ALGN", "ALXN", "AMAT", "AMD", "AMGN",
    "ANSS", "ASML", "ATVI", "AVGO", "BIDU", "BIIB", "BKNG", "BMRN", "CDNS", "CDW",
    "CERN", "CHKP", "CHTR", "CMCSA", "COST", "CPRT", "CSCO", "CSX", "CTAS", "CTSH",
    "CTXS", "DLTR", "DOCU", "DXCM", "EA", "EBAY", "EXC", "EXPE", "FAST", "FB",
    "FISV", "FOX", "FOXA", "GILD", "GOOG", "GOOGL", "IDXX", "ILMN", "INCY", "INTC",
    "INTU", "ISRG", "JD", "KDP", "KHC", "KLAC", "LRCX", "LULU", "LUMN", "LVGO",
    "MAR", "MCHP", "MDLZ", "MELI", "MNST", "MRNA", "MSFT", "MU", "MXIM", "NFLX",
    "NTAP", "NTES", "NVDA", "NXPI", "OKTA", "ORLY", "PAYX", "PCAR", "PDD", "PEP",
    "PYPL", "QCOM", "REGN", "ROST", "SBUX", "SGEN", "SIRI", "SNPS", "SPLK", "SWKS",
    "TCOM", "TEAM", "TMUS", "TSLA", "TXN", "VRSK", "VRTX", "WBA", "WDAY", "XEL",
    "XLNX", "ZM"
]

def get_ticker_data(presets: tuple, client: RESTClient):
    ticker, multiplier, timespan, start, end, limit = presets
    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=multiplier, timespan=timespan, from_=start, to=end, limit=limit):
        aggs.append(a)

    df = pd.DataFrame(aggs)
    filepath = Path('data/raw/'+str(ticker).lower()+'/'+str(ticker).lower()+"_"+str(multiplier)+"_"+timespan+"_data_raw.csv")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath)

# connect to API
client = RESTClient(api_key="")

start = '2018-01-01'
end = '2024-01-01'
limit = 50000

# daily data
for ticker in sp500_tickers:
    presets = (ticker,1,'day',start,end,limit)
    get_ticker_data(presets, client)

# hourly data
for ticker in sp500_tickers:
    presets = (ticker,1,'hour',start,end,limit)
    get_ticker_data(presets, client)
    presets = (ticker,4,'hour',start,end,limit)
    get_ticker_data(presets, client)