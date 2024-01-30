import pandas as pd
from app.pipeline.transform import concat_data_frames

data_1 =pd.DataFrame( {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 28],
    'Cidade': ['São Paulo', 'Nova York', 'Londres', 'Tóquio']
})

data_2 = pd.DataFrame({
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 28],
    'Cidade': ['São Paulo', 'Nova York', 'Londres', 'Tóquio']
})

#Teste unitário
def testar_a_concatenacao_da_lista_de_dataframe():
    arrange = pd.concat([data_1, data_2], ignore_index=True)
    act = concat_data_frames([data_1, data_2])
 
    assert arrange.equals(act)