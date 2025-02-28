import streamlit as st

st.header ("Aluno")


st.multiselect (
  'Quais são suas corers favoritas?',
  ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
  ['Amarelo', 'Vermelho',])

st.color_picker("Escolha a Cor", "#00f900")
st.feedback("stars")

st.toggle ("Toggle")
st.text_area ("Text de caixa Grande")
st.text_input ("Text ants da Caixa", "Texto fraco na Caixa")

st.selectbox (
  'Qual a sua cor favorita?', 
  ('Azul', 'Vermelho', 'Verde'))

st.checkbox ('Sorvete')
st.checkbox ('Banana')
st.checkbox ('Chocolate')

options = ["Norte", "Sul", "Leste", "Oeste"]
selection = st.pills("Directions", options, selection_mode="multi")

st.button ("Botão Salvar")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.button ("Reset")
