import os
import pandas as pd


"""
Receber um dataframe e salvar como excel

args: 
    dataframe (pd.Dataframe)
    output_file(str): caminho onde será salvo
    file_name (str): nome do arquivo a ser salvo

return: "Arquivo salvo com sucesso"
"""

def load_excel(data_frame, output_path, file_name):

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"