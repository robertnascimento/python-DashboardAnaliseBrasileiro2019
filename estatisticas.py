import r38copia as r38


# Time que tomou mais gols
time_mais_gols_sofridos = r38.rodada_38[r38.rodada_38['Gols_contra'] == r38.rodada_38['Gols_contra'].max()]['Time'].values[0]
total_gols_sofridos = r38.rodada_38['Gols_contra'].max()

# Time que marcou mais gols
time_mais_gols_marcados = r38.rodada_38[r38.rodada_38['Gols_pro'] == r38.rodada_38['Gols_pro'].max()]['Time'].values[0]
total_gols_marcados = r38.rodada_38['Gols_pro'].max()

# Time que sofreu menos gols
time_menos_gols_sofridos = r38.rodada_38[r38.rodada_38['Gols_contra'] == r38.rodada_38['Gols_contra'].min()]['Time'].values[0]
total_gols_menos_sofridos = r38.rodada_38['Gols_contra'].min()

# Time com mais vitórias
time_mais_vitorias = r38.rodada_38[r38.rodada_38['Vitoria'] == r38.rodada_38['Vitoria'].max()]['Time'].values[0]
total_vitorias = r38.rodada_38['Vitoria'].max()

# Time com mais derrotas
time_mais_derrotas = r38.rodada_38[r38.rodada_38['Derrota'] == r38.rodada_38['Derrota'].max()]['Time'].values[0]
total_derrotas = r38.rodada_38['Derrota'].max()

# Time com mais empates
time_mais_empates = r38.rodada_38[r38.rodada_38['Empate'] == r38.rodada_38['Empate'].max()]['Time'].values[0]
total_empates = r38.rodada_38['Empate'].max()

# Encontrar o time com mais pontos
time_mais_pontos = r38.rodada_38[r38.rodada_38['Pontos'] == r38.rodada_38['Pontos'].max()]['Time'].values[0]
total_pontos = r38.rodada_38['Pontos'].max()