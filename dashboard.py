import streamlit as st
import numpy as np
import pandas as pd
import analise as an
import rodadafinal as r38
import gols as gol
import jogomaisgols as jmg
import dobromedia as dm
import estatisticas as est
import flamengo as fla

st.title("ANÁLISE BRASILEIRO 2019")
st.write('\n\n')

st.subheader("TABELA FINAL")
st.table(r38.rodada_38)

st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')


gols = {
     "Equipes": ["Visitantes", "Mandantes","Total de gols"],
     "Valores": [gol.soma_gols_visitante_2019, gol.soma_gols_mandante_2019, gol.soma_gols_total_br],
}

golsdata = pd.DataFrame(gols)
st.subheader("COMPARATIVO DE GOLS ")
st.bar_chart(golsdata.set_index("Equipes"), width=0.5)

st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')

# Seus dados de média de gols

v = round(gol.media_gols_visitante,2)
r = round(gol.media_gols_rodada,2)
m = round(gol.media_gols_mandante,2)

media_gols = {
    "Equipes": ["Visitantes", "Mandantes", "Total de gols"],
    "Valores": [v, m, r]  # Substitua esses valores pelas suas médias reais
}

# Criando o DataFrame com os dados de média de gols
mediagolsdata = pd.DataFrame(media_gols)

# Exibindo o gráfico de barras
st.subheader("MÉDIA DE GOLS ")
st.bar_chart(mediagolsdata.set_index("Equipes")["Valores"], width=0.5)


st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')


st.header("ㅤㅤㅤㅤㅤJOGO COM MAIS GOLS")
jmg.exibir_placar(jmg.jogo_mais_gols['Rodada'], jmg.jogo_mais_gols['Mandante'], jmg.jogo_mais_gols['Mandante Placar'],jmg.jogo_mais_gols['Visitante Placar'], jmg.jogo_mais_gols['Visitante'])

st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')

st.subheader("Jogos em que o time venceu por uma vantagem que é o dobro da mediana")
st.table(dm.jogos_vitoria_dobro_mediana[['Mandante', 'Visitante', 'Mandante Placar', 'Visitante Placar', 'Diferenca Gols']])

st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')



st.header("Estatísticas da Temporada")
st.write(f"ㅤㅤTime com mais pontos {est.time_mais_pontos}: {est.total_pontos} pontos.")
st.write(f"ㅤㅤTime que marcou mais gols {est.time_mais_gols_marcados}: {est.total_gols_marcados} gols marcados.")
st.write(f"ㅤㅤTime que tomou mais gols {est.time_mais_gols_sofridos}: {est.total_gols_sofridos} gols sofridos.")
st.write(f"ㅤㅤTime que sofreu menos gols {est.time_menos_gols_sofridos}: {est.total_gols_menos_sofridos} gols sofridos.")
st.write(f"ㅤㅤTime com mais vitórias {est.time_mais_vitorias}: {est.total_vitorias} vitórias.")
st.write(f"ㅤㅤTime com mais derrotas {est.time_mais_derrotas}: {est.total_derrotas} derrotas.")
st.write(f"ㅤㅤTime com mais empates {est.time_mais_empates}: {est.total_empates} empates.")



st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')

st.title("CAMPEÃO BRASILEIRO 2019")

col1, col2 = st.columns([1, 2]) 


with col1:
    imagem_url = "flamengo.png"
    st.image(imagem_url, width=200)

with col2:
    st.subheader(f"Flamengo")

    dados_flamengo = {
        "Categoria": ["Vitórias", "Empates", "Derrotas", "Saldo de gols", "Gols marcados", "Gols sofridos"],
        "Quantidade": [fla.quantidade_vitorias_flamengo, fla.quantidade_empates_flamengo, 
                       fla.quantidade_derrotas_flamengo, fla.quantidade_saldo_de_gols_flamengo, 
                       fla.quantidade_golspro_flamengo, fla.quantidade_gols_contra_flamengo]
    }
    tabela_flamengo = pd.DataFrame(dados_flamengo)
    tabela_flamengo.index = np.arange(1, len(tabela_flamengo) + 1)  # Correção aqui

    st.table(tabela_flamengo)



st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')

st.title("CLASSIFICADOS PARA LIBERTADORES")

col1, col2 = st.columns([1, 2]) 

with col1:
    imagem_url = "copa-libertadores.png"
    st.image(imagem_url, width=200)

with col2:
    seis_primeiros = r38.rodada_38.head(6)["Time"]  # Pegando somente o nome dos times

    dados_tabela = {
        "Vaga": ["Libertadores"] * 4 + ["Pré-Libertadores"] * 2,
        "Time": seis_primeiros.tolist()
    }
    
    tabela_classificacao_liberta = pd.DataFrame(dados_tabela)
    tabela_classificacao_liberta.index = np.arange(1, len(tabela_classificacao_liberta) + 1)  # Correção do índice

    st.table(tabela_classificacao_liberta)





st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')


st.title("CLASSIFICADOS PARA SUL-AMERICANA")

col1, col2 = st.columns([1, 2]) 

with col1:
    imagem_url = "copa-sulamericana-logo.png"
    st.image(imagem_url, width=200)

with col2:
    setimo_ate_doze = r38.rodada_38.iloc[6:12]["Time"]  # Pegando o nome dos times do 7º ao 12º

    dados_tabela = {
        "Vaga": ["Sul-americana"] * 6,  # Categorizando como Pré-Libertadores
        "Time": setimo_ate_doze.tolist()  # Convertendo para lista
    }
    
    tabela_classificacao_Sulamericana = pd.DataFrame(dados_tabela)
    tabela_classificacao_Sulamericana.index = np.arange(7, len(tabela_classificacao_Sulamericana) + 7)  # Ajustando o índice

    st.table(tabela_classificacao_Sulamericana)








st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
st.write('\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ\nㅤ')


st.title("REBAIXADOS")

col1, col2 = st.columns([1, 2]) 

with col1:
    imagem_url = "Campeonato_Brasileiro_Série_B_logo.png"
    st.image(imagem_url, width=200)

with col2:
    rbr = r38.rodada_38.iloc[16:22]["Time"]  # Pegando o nome dos times do 17º ao 22º

    dados_tabela = {
        "Despromoção": ["Rebaixado"] * len(rbr),  # Ajustando a quantidade de elementos para corresponder a rbr
        "Time": rbr.tolist()
    }
    
    tabela_rebaixados = pd.DataFrame(dados_tabela)
    tabela_rebaixados.index = np.arange(17, len(tabela_rebaixados) + 17)  # Ajustando o índice

    st.table(tabela_rebaixados)
