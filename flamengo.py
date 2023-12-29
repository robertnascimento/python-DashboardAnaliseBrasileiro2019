import r38copia as r38

# Filtrar os dados do Flamengo na rodada 38
flamengo_rodada_38 = r38.rodada_38[r38.rodada_38['Time'] == 'Flamengo']

# Contar a quantidade de vitorias do Flamengo na rodada 38
quantidade_vitorias_flamengo = flamengo_rodada_38['Vitoria'].sum()

# Contar a quantidade de empates do Flamengo na rodada 38
quantidade_empates_flamengo = flamengo_rodada_38['Empate'].sum()

# Contar a quantidade de derrotas do Flamengo na rodada 38
quantidade_derrotas_flamengo = len(flamengo_rodada_38[flamengo_rodada_38['Derrota'] > 0])

# Contar a quantidade de gols pro do Flamengo na rodada 38
quantidade_golspro_flamengo = flamengo_rodada_38['Gols_pro'].sum()

# Contar a quantidade de gols contra do Flamengo na rodada 38
quantidade_gols_contra_flamengo = flamengo_rodada_38['Gols_contra'].sum()

# Contar a quantidade de empates do Flamengo na rodada 38
quantidade_saldo_de_gols_flamengo = flamengo_rodada_38['Saldo_de_gols'].sum()

print(f"Flamengo teve {quantidade_vitorias_flamengo} vitórias, {quantidade_empates_flamengo} empates, {quantidade_derrotas_flamengo} derrotas, seu saldo de gols ao final do campeonato foi de {quantidade_saldo_de_gols_flamengo} gol na rodada 38.")
print(f"o Flamengo tomou {quantidade_gols_contra_flamengo} gols, é marcou {quantidade_golspro_flamengo} gols.")
