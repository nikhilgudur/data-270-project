from utils import get_coin_data_csv, get_coin_data_df

if __name__ == "__main__":
    # Fetch data for the following coins and save them as CSV files
    get_coin_data_csv("btc", "bitcoin")
    get_coin_data_csv("eth", "ethereum")
    get_coin_data_csv("aave", "aave")
    get_coin_data_csv("doge", "dogecoin")

    btc_df = get_coin_data_df("btc", "bitcoin")
    eth_df = get_coin_data_df("eth", "ethereum")
    aave_df = get_coin_data_df("aave", "aave")
    doge_df = get_coin_data_df("doge", "dogecoin")

    # print(btc_df.info())

    print(btc_df.isna().sum())

    print(eth_df.isna().sum())
    print(aave_df.isna().sum())
    print(doge_df.isna().sum())
