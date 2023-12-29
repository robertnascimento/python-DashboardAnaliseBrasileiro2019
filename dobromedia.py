import streamlit as st
import pandas as pd
import numpy as np

# Lendo o arquivo com os dados das rodadas
rdd = pd.read_csv('df_rodadas.csv')

# Filtrando para considerar apenas a temporada de 2019
rdd2019 = rdd[rdd['Temporada'] == 2019]

# Calcular a diferença de gols por partida
rdd2019['Diferenca Gols'] = abs(rdd2019['Mandante Placar'] - rdd2019['Visitante Placar'])

# Calcular a mediana das diferenças de gols
mediana_diferenca_gols = rdd2019['Diferenca Gols'].median()

# Calcular o dobro da mediana
dobro_mediana = 2 * 2

# Filtrar os jogos onde a diferença de gols é maior ou igual ao dobro da mediana
jogos_vitoria_dobro_mediana = rdd2019[(rdd2019['Diferenca Gols'] >= dobro_mediana) & (rdd2019['Mandante Placar'] > rdd2019['Visitante Placar']) | (rdd2019['Diferenca Gols'] >= dobro_mediana) & (rdd2019['Mandante Placar'] < rdd2019['Visitante Placar'])]

# Resetando o índice para remover a coluna de índice
jogos_vitoria_dobro_mediana = jogos_vitoria_dobro_mediana.reset_index(drop=True)
jogos_vitoria_dobro_mediana.index = np.arange(1, len(jogos_vitoria_dobro_mediana) + 1)