import pandas as pd
import numpy as np

br = pd.read_csv('df_classificacao.csv')
rdd = pd.read_csv('df_rodadas.csv')

br2019 = br[br['Temporada'] == 2019]
rdd2019 = rdd[rdd['Temporada'] == 2019]

# Criar uma cópia do DataFrame para evitar o aviso
rdd2019 = rdd2019.copy()

# Somar os gols dos mandantes e visitantes para a temporada de 2019
soma_gols_mandante_2019 = rdd2019['Mandante Placar'].sum()
soma_gols_visitante_2019 = rdd2019['Visitante Placar'].sum()
soma_gols_total_br = soma_gols_mandante_2019 + soma_gols_visitante_2019

media_gols_mandante = rdd2019['Mandante Placar'].mean()
media_gols_visitante = rdd2019['Visitante Placar'].mean()
media_gols_rodada = media_gols_mandante + media_gols_visitante