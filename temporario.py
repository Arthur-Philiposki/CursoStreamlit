import streamlit as st

st.header ("Cabeçalho")
st.multiselect (
  'Quais são suas corers favoritas?',
  ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
  ['Amarelo', 'Vermelho',])
st.toggle ("Toggle")
st.text_area ("Text de caixa Grande")
st.text_input ("Text ants da Caixa", "Texto fraco na Caixa")
st.selectbox (
  'Qual a sua cor favorita?', 
  ('Azul', 'Vermelho', 'Verde'))
st.button ("Botão Salvar")

