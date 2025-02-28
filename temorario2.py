import streamlit as st

st.header ("Aluno")

st.text_input ("Nome", "Digite o nome do Aluno")

number = st.number_input(
    "Numero do CPF", value=None, placeholder="Digite o CPF do Aluno..."
)


number = st.number_input(
    "Numero do RG", value=None, placeholder="Digite o RG do Aluno..."
)


number = st.number_input(
    "Numero do RA", value=None, placeholder="Digite o RA do Aluno..."
)

st.text_input ("Data Nascimento", "Digite a Data de Nascimento")

st.button ("Salvar")
