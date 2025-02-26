import streamlit as st

st.header ("Cabeçalho")
st.toggle ("Toggle")
st.text_area ("Text de caixa Grande")
st.text_input ("Text ants da Caixa", "Texto fraco na Caixa")
st.select (
  'Qual a sua cor favorita?', 
  ('Azul', 'Vermelho', 'Verde'))
st.button ("Botão Salvar")

