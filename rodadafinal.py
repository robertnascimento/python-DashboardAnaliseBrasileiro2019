import pandas as pd
import numpy as np

br = pd.read_csv('df_classificacao.csv')
rdd = pd.read_csv('df_rodadas.csv')

br2019 = br[br['Temporada'] == 2019]
rdd2019 = rdd[rdd['Temporada'] == 2019]


rodada_38 = br2019[(br2019['Temporada'] == 2019) & (br2019['Rodada'] == 38)]
rodada_38 = rodada_38.reset_index(drop=True)
rodada_38 = rodada_38.drop(['Gols_pro',
                            'Gols_contra',
                            'Saldo_de_gols',
                            'Vitorias_consecutivas',
                            'Derrotas_consecutivas',
                            'Jogos_marcando',
                            'Posicao',
                            'Jogos_sem_sofrer_gols',
                            'Temporada'], axis=1)

colunas = rodada_38.columns.tolist()
colunas.insert(1, colunas.pop(colunas.index('Pontos')))
rodada_38 = rodada_38[colunas]

rodada_38.reset_index(drop=True, inplace=True)
rodada_38.index = np.arange(1, len(rodada_38) + 1)