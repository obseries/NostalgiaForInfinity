import re

# row = "elif (last_candle['r_14'] > -18.0) and (last_candle['rsi_14'] > 64.0) and (last_candle['cti'] > 0.9) and (last_candle['sma_200_dec_20_15m']) and (last_candle['sma_200_dec_20_1h']) and (last_candle['cmf'] < -0.0) and (last_candle['cmf_15m'] < -0.0) and (last_candle['r_96_15m'] < -50.0) and (last_candle['r_480_1h'] < -50.0):"
row = "item_buy_protection_list.append(dataframe['close'] > dataframe[f\"ema_{global_buy_protection_params['close_above_ema_slow_len']}_1h\"])"

info_timeframe_1d = '1d'
info_timeframe_1h = '1h'
info_timeframe_15m = '15m'

# f"ema_{global_buy_protection_params['ema_slow_len']}_1h"

row_cleaned = re.sub('\'([a-za-zA-Z0-9_]*)_15m\'', 'f"\\1_{info_timeframe_15m}"', row)
row_cleaned = re.sub('\'([a-za-zA-Z0-9_]*)_1h\'', 'f"\\1_{info_timeframe_1h}"', row_cleaned)
row_cleaned = re.sub('\'([a-za-zA-Z0-9_]*)_1d\'', 'f"\\1_{info_timeframe_1d}"', row_cleaned)
row_cleaned = re.sub('f"([a-za-zA-Z0-9_{}[\\]\']*)_1h"', 'f"\\1_{info_timeframe_1h}"', row_cleaned)

print(row)
print(row_cleaned)


lines = []
with open('NostalgiaForInfinityX.py') as f:
    lines = f.readlines()

with open('NostalgiaForInfinityX-out.py', 'w') as f:
    for line in lines:
        line_cleaned = re.sub('\'([a-za-zA-Z0-9_]*)_15m\'', 'f"\\1_{self.info_timeframe_15m}"', line)
        line_cleaned = re.sub('\'([a-za-zA-Z0-9_]*)_1h\'', 'f"\\1_{self.info_timeframe_1h}"', line_cleaned)
        line_cleaned = re.sub('\'([a-za-zA-Z0-9_]*)_1d\'', 'f"\\1_{self.info_timeframe_1d}"', line_cleaned)
        line_cleaned = re.sub('f"([a-za-zA-Z0-9_{}[\\]\']*)_15m"', 'f"\\1_{self.info_timeframe_15m}"', line_cleaned)
        line_cleaned = re.sub('f"([a-za-zA-Z0-9_{}[\\]\']*)_1h"', 'f"\\1_{self.info_timeframe_1h}"', line_cleaned)
        line_cleaned = re.sub('f"([a-za-zA-Z0-9_{}[\\]\']*)_1d"', 'f"\\1_{self.info_timeframe_1d}"', line_cleaned)

        f.write(line_cleaned)
#        f.write('\n')