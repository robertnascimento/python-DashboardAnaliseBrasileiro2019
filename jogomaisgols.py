import streamlit as st
import pandas as pd

rdd2019 = pd.read_csv('df_rodadas.csv')

def exibir_placar(numero_rodada, time_mandante, gols_mandante, gols_adversario, time_adversario):
    html = f"""
    <div style="text-align: center; font-size: 20px; margin-bottom: 20px;">
        <span style="font-size: 28px;">Rodada {numero_rodada}</span>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
            <div style="flex: 1; text-align: right; margin-right: 10px;">
                {time_mandante}
            </div>
            <div style="font-size: 28px; margin-right: 10px;">
                {gols_mandante} - {gols_adversario}
            </div>
            <div style="flex: 1; text-align: left; margin-left: 10px;">
                {time_adversario}
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


rdd2019 = rdd2019[rdd2019['Temporada'] == 2019].copy()
rdd2019.loc[:, 'Total Gols Partida'] = rdd2019['Mandante Placar'] + rdd2019['Visitante Placar']
jogo_mais_gols = rdd2019.loc[rdd2019['Total Gols Partida'].idxmax()]