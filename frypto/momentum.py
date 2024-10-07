import pandas as pd
import numpy as np
from helpers import _calculate_roc, _calculate_rsi, _calculate_macd

class MomentumFeatures:
    def __init__(self, close: np.ndarray) -> None:
        self.close = close
        

    def compute(self, window: int = 15, rsi_window: int = 14, macd_windows: tuple = (12, 26, 9)) -> pd.DataFrame:
        
        df = pd.DataFrame()
        # RSI Calculation
        df['RSI'] = _calculate_rsi(self.close, rsi_window)

        # MACD and Signal Line
        macd, signal_line = _calculate_macd(self.close, macd_windows[0], macd_windows[1], macd_windows[2])
        df['MACD'] = macd
        df['Signal_Line'] = signal_line

        # SMA and EMA
        sma = np.mean(np.lib.stride_tricks.sliding_window_view(self.close, window), axis=1)
        df['SMA'] = np.concatenate([[np.nan] * (window - 1), sma])
        df['EMA'] = pd.Series(self.close).ewm(span=window, adjust=False).mean()

        # Rate of Change (ROC)
        df['ROC'] = _calculate_roc(self.close, window)

        return df