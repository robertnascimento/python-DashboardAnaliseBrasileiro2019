import pandas as pd
import numpy as np

br = pd.read_csv('df_classificacao.csv')
rdd = pd.read_csv('df_rodadas.csv')

br2019 = br[br['Temporada'] == 2019]
rdd2019 = rdd[rdd['Temporada'] == 2019]


rodada_38 = br2019[(br2019['Temporada'] == 2019) & (br2019['Rodada'] == 38)]