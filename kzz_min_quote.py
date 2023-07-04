import efinance as ef
import os
from datetime import datetime

os.environ['NO_PROXY'] = '*'


def download_kzz_min():
    # 获取可转债实时行情
    kzz_spot = ef.bond.get_realtime_quotes()
    kzz_spot_top = kzz_spot[:100].copy()

    today = datetime.now().strftime("%Y%m%d")

    save_dir = f"./data/{today}/min"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    kzz_spot_top.to_csv(f"./data/{today}/kzz_spot_top.csv")

    # 遍历
    for index, row in kzz_spot_top.iterrows():
        kzz_min_df = ef.bond.get_quote_history(row["债券代码"], beg=today, end=today, klt=1)
        kzz_min_df.to_csv(f"./data/{today}/min/{row['债券代码']}.csv")


if __name__ == '__main__':
    download_kzz_min()
