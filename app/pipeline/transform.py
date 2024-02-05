import pandas as pd

"""
Função para transformar uma lista de dataframes
 em um único dataframe consolidado
"""


def concat_data_frames(data_frame_list):
    return pd.concat(data_frame_list, ignore_index=True)
