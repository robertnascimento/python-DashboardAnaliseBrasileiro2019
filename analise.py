import numpy as np
import pandas as pd

br = pd.read_csv('df_classificacao.csv')
rdd = pd.read_csv('df_rodadas.csv')

br2019 = br[br['Temporada'] == 2019]
rdd2019 = rdd[rdd['Temporada'] == 2019]


soma_gols_mandante_2019 = rdd2019['Mandante Placar'].sum()
soma_gols_visitante_2019 = rdd2019['Visitante Placar'].sum()
soma_gols_total_br = soma_gols_mandante_2019 + soma_gols_visitante_2019


