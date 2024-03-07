Includes a Hidden Markov Model for Daily, 4 Hour, and 1 Hour timeframes. Trained models are available, performance of each model is recorded, data analysis is started.

HMM
TO DO:
- automate model updates
- add recompile strategies
- finish live prediction for 1 hour and 4 hour 15min and 5min
- run crypto models

CV Pattern:
TO DO:
- label data
- start training

Stock Image:
- Begin Training

Crypto AI
- get 4hr and 1hr data
- train model for (asia/eu/us) market times
    - crypto 24hr, traders in each timezone have different habbits
    - allow model to pick up more patterns
- remove weekend data
    - do some data discovery by checking the average change in price from
    friday 20UTC to sunday 20UTC
    - is it worth cutting out, do weekend move matter and if so how much?
- BEAR MARKET GAP Filling
    - price jumps in bear maket, chance of reversale, average run up after jumps
        - track the lows and high of previous cliffs, apply percentages of chance of reaching
        - use markov chains?

Stock AI 
- finish gathering MAPE data
- finish gathering 4hr and 1hr images
- reformat the predicted data
- create candel chart using the highs and lows and chart besside each other

QUALITY OF LIFE
- find may to make sp500 array available to all classes
- abstract out the stock predictor from the training predictor

General All
- create a script to test the next period data, given last 10 period data
    - live pull the data
    - automated 

- create bear and bull models
        - split data bull market vs bear market

DATA SCIENCE STUFF:
- look at the average return of new coinbase listings after list
