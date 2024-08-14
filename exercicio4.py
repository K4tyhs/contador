import streamlit as st

st.title("Calcule ano, mês e dia")
st.sidebar.header("Me informe algumas coisas:")
nascimento = st.sidebar.number_input("Qual o seu ano de nascimento", min_value=1500, max_value=2100, step=1)
atual = st.sidebar.number_input("Qual é o ano atual?", min_value=1500, max_value=2100, step=1)

if st.button("calcular_bottom"):
  ano = atual - nascimento
  mes = ano * 12
  dia = ano * 365
  st.success(f"Você tem {ano} anos, {mes} meses e {dia} dias aproximadamente.")
