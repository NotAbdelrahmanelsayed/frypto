import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from typing import Tuple
def _pad_nan(values: np.ndarray, window: int) -> np.ndarray:
        """Pad the array with NaN values at the beginning to match the original array length."""
        return np.concatenate([np.full(window - 1, np.nan), values])

def _calculate_roc(close: np.ndarray, window: int) -> np.ndarray:
        return ((close - np.roll(close, window)) / np.roll(close, window)) * 100

def _calculate_rsi(close: np.ndarray, window: int) -> np.ndarray:
        """Relative Strength Index (RSI) Calculation."""
        delta = np.diff(close, prepend=close[0])
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)

        avg_gain = np.convolve(gain, np.ones(window)/window, mode='valid')
        avg_loss = np.convolve(loss, np.ones(window)/window, mode='valid')

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return np.concatenate([[np.nan] * (window - 1), rsi])
# def _calculate_dmi(window=14):
#         """Directional Movement Index (DMI) Calculation."""
#         delta_high = np.diff(high_np, prepend=high_np[0])
#         delta_low = np.diff(low_np, prepend=low_np[0])

#         plus_dm = np.where((delta_high > delta_low) & (delta_high > 0), delta_high, 0)
#         minus_dm = np.where((delta_low > delta_high) & (delta_low > 0), delta_low, 0)

#         true_range = high_np - low_np
#         atr = np.mean(np.lib.stride_tricks.sliding_window_view(true_range, window), axis=1)
#         atr = np.concatenate([[np.nan] * (window - 1), atr])

#         plus_di = 100 * (np.convolve(plus_dm, np.ones(window) / window, mode='valid') / atr[window - 1:])
#         minus_di = 100 * (np.convolve(minus_dm, np.ones(window) / window, mode='valid') / atr[window - 1:])

#         dx = 100 * np.abs((plus_di - minus_di) / (plus_di + minus_di))
#         adx = np.convolve(dx, np.ones(window) / window, mode='valid')

#         plus_di = np.concatenate([[np.nan] * (window - 1), plus_di])
#         minus_di = np.concatenate([[np.nan] * (window - 1), minus_di])
#         adx = np.concatenate([[np.nan] * (window * 2 - 2), adx])

#         return plus_di, minus_di, adx

# def _calculate_trend_lines(close: np.ndarray, window: int = 20) -> pd.Series:
#         """Support and Resistance Lines Calculation."""
#         local_min = argrelextrema(close, np.less_equal, order=window)[0]
#         support_line = pd.Series(close[local_min], index=local_min)

#         local_max = argrelextrema(close, np.greater_equal, order=window)[0]
#         resistance_line = pd.Series(close[local_max], index=local_max)

#         return support_line, resistance_line

# def _calculate_ichimoku_cloud() -> pd.DataFrame:
#         """Ichimoku Cloud Calculation."""
#         tenkan_window = 20
#         kijun_window = 60
#         senkou_span_b_window = 120
#         cloud_displacement = 30
#         chikou_shift = -30

#         tenkan_sen = (pd.Series(high_np).rolling(window=tenkan_window).max() + pd.Series(low_np).rolling(window=tenkan_window).min()) / 2
#         df['tenkan_sen'] = tenkan_sen

#         kijun_sen = (pd.Series(high_np).rolling(window=kijun_window).max() + pd.Series(low_np).rolling(window=kijun_window).min()) / 2
#         df['kijun_sen'] = kijun_sen

#         df['senkou_span_a'] = ((tenkan_sen + kijun_sen) / 2).shift(cloud_displacement)

#         senkou_span_b = (pd.Series(high_np).rolling(window=senkou_span_b_window).max() + pd.Series(low_np).rolling(window=senkou_span_b_window).min()) / 2
#         df['senkou_span_b'] = senkou_span_b.shift(cloud_displacement)

#         df['chikou_span'] = df['Close'].shift(chikou_shift)

#         return df

def _calculate_macd(
                close: np.ndarray, short_window: int = 12,\
                long_window: int = 26, signal_window: int = 9
) -> Tuple[np.ndarray, np.ndarray]:
        
        """MACD Calculation."""
        ema_12 = pd.Series(close).ewm(span=short_window, adjust=False).mean().values
        ema_26 = pd.Series(close).ewm(span=long_window, adjust=False).mean().values
        macd = ema_12 - ema_26
        signal_line = pd.Series(macd).ewm(span=signal_window, adjust=False).mean().values
        return macd, signal_line

