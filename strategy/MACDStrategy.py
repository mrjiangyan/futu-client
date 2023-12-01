from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader as bt
from .BaseStrategy import BaseStrategy
from loguru import logger
import pandas as pd

class MACDStrategy(BaseStrategy):
    params = (
        ("short_period", 12),
        ("long_period", 26),
        ("signal_period", 9),
        ("macd_level", -0.5),
        ("period", 9),
        ("k_period", 3),
        ("d_period", 3),
        ("kdj_j_threshold", 20)
    )

    def __init__(self):
         # Add your MACD indicator here
        self.macd = bt.indicators.MACD()

        # Add Bollinger Bands
        self.bollinger = bt.indicators.BollingerBands()
        self.kdj = bt.indicators.StochasticFull(
            period= self.params.period,
            period_dfast=self.params.k_period,
            period_dslow=self.params.d_period,
        )

         # Add a Simple Moving Average (SMA) for the rolling mean of volume
        self.avg_5d_volume = bt.indicators.SimpleMovingAverage(self.data.volume, period=5)
        
        self.avg_10d_volume = bt.indicators.SimpleMovingAverage(self.data.volume, period=10)

        self.close_prices = self.data.close.get(size=15)  # 获取最近15天的收盘价
       
        
        if len(self.close_prices) >= 2:
            self.price_change_15d = (self.close_prices[-1] - self.close_prices[0]) / self.close_prices[0] * 100
        else:
            self.price_change_15d  = None
            # print(self.close_prices)
            # Handle the case when there are not enough elements in close_prices
            # print("Insufficient data in close_prices.")

    def next(self):
        
        current_price = self.data.close[0]
        macd_value = self.macd.lines.macd[0]
        signal_value = self.macd.lines.signal[0]
        
        stoch_k_current = self.kdj.lines.percK[0]
        stoch_d_current = self.kdj.lines.percD[0]
        stoch_j_current =self.kdj.lines.percDSlow[0]

        
        j = self.kdj.percD[0] * 3 - self.kdj.percDSlow[0] * 2
        # print(self.datas[0].datetime.datetime(0), stoch_k_current, stoch_d_current, stoch_j_current)
        # print(self.datas[0].datetime.datetime(0),j, self.kdj.percK[0], self.kdj.percD[0], self.kdj.percDSlow[0])
        # MACD出现日线的金叉，但是
        buy_signal = (self.macd.macd[0] > self.macd.signal[0] and 
                      self.macd.macd[-1] <= self.macd.signal[-1] and
                      self.macd.macd[0] < -0.5 and self.macd.signal[0] < -0.5 
                      and stoch_j_current < self.params.kdj_j_threshold
                    #   self.avg_5d_volume[-1] < self.avg_10d_volume[-1] and
                    #   self.avg_5d_volume[0] > self.avg_10d_volume[0] 
                      )
        
        if buy_signal and self.price_change_15d != None:
            buy_signal =  self.price_change_15d < -10 
        
        sell_signal = (self.macd.macd[0] < self.macd.signal[0] and 
                       self.macd.macd[-1] >= self.macd.signal[-1] and 
                       self.macd.macd[0] > 0 )
        
        if buy_signal:
            if self.internal_buy() == True:
                print(j, self.kdj.percK[0], self.kdj.percD[0], self.kdj.percDSlow[0])
                logger.info(f'{self.macd.macd[0]}, {self.macd.signal[0]}')
            
        elif sell_signal:
            self.internal_sell()