import os
import pickle
from pathlib import Path
import pandas as pd


def get_data(subset=None):
    data_path = Path(os.getcwd()) / Path("data/df_dashboard.pkl")
    with open(data_path, mode='rb') as file:
        df = pickle.load(file)
        # nötig, da pd.concat ansonsten später nicht funktioniert
        df_dict = df.to_dict()
        df = df.from_dict(df_dict)
    return data_transformation(df, subset)


def get_data_v2(subset=None):
    data_path = Path(os.getcwd()) / Path("data/df_dashboard_v2.pkl")
    df = pd.read_pickle(data_path)
    return data_transformation(df, subset)


def data_transformation(df, subset=None):
    if subset is None:
        subset = ['food_supply_kilocalories_per_person_and_day', "sugar_per_person_g_per_day"]
    df.drop(columns=['country'], inplace=True, errors='ignore')
    df_regions = df.copy(deep=True)
    df_regions = df_regions.drop(columns=['geo', 'name'])

    df_gruppiert = df_regions.groupby(['year', 'world_4region']).mean().reset_index().dropna(subset=subset)
    df_gruppiert.rename(columns={'world_4region': 'geo'}, inplace=True)
    df_gruppiert['geo'].replace({'americas': 'america'}, inplace=True)
    df_gruppiert['name'] = (df_gruppiert['geo'].apply(lambda x: x.capitalize())) + " (mean)"

    df.drop(columns=['world_4region'], inplace=True)
    return pd.concat([df.reset_index(drop=True), df_gruppiert.reset_index(drop=True)], axis=0, ignore_index=True)
