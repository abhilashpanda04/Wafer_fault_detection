#get the data from datasource 
#save it to data/raw for further process


import os
from get_data import read_params,get_data
import argparse
# from rich.traceback import install
# install(show_locals=True)


def load_and_save(config_path):
    config=read_params(config_path)
    dataframe=get_data(config_path)
    new_cols=[col.replace(" ","_") for col in dataframe.columns]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    dataframe.to_csv(raw_data_path,index=False,columns=new_cols)
    print(dataframe.head())

if __name__ == "__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args=args.parse_args()
    load_and_save(config_path=parsed_args.config)