import streamlit as st

st.set_page_config(page_title="Identificação de Enterobactérias", page_icon="🧫")

st.title("🦠 Identificação de Enterobactérias por Testes Bioquímicos")
st.write("Preencha os campos abaixo com os resultados dos testes:")

# Formulário
indol = st.selectbox("Indol", ["Negativo", "Positivo"])
citrato = st.selectbox("Citrato", ["Negativo", "Positivo"])
h2s = st.selectbox("Produção de H2S", ["Negativo", "Positivo"])
urease = st.selectbox("Urease", ["Negativo", "Positivo"])
lisina = st.selectbox("Lisina", ["Negativo", "Positivo"])
motilidade = st.selectbox("Motilidade a 35°C", ["Negativo", "Positivo"])
sacarose = st.selectbox("Sacarose", ["Negativo", "Positivo"])
gasdaglicose = st.selectbox("Gás da glicose", ["Negativo", "Positivo"])

dados = (indol, citrato, h2s, urease, lisina, motilidade, sacarose, gasdaglicose)

# Dicionário de identificação
tabela_identificacao = {
    ('Positivo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo'): 'Citrobacter diversus',
    ('Negativo', 'Positivo', 'Positivo', 'Negativo', 'Negativo', 'Positivo', 'Positivo', 'Positivo'): 'Citrobacter freundii',
    ('Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Positivo'): 'Edwardsiella tarda',
    ('Negativo', 'Positivo', 'Negativo', 'Negativo', 'Positivo', 'Positivo', 'Positivo', 'Positivo'): 'Enterobacter agglomerans',
    ('Negativo', 'Positivo', 'Negativo', 'Negativo', 'Negativo', 'Positivo', 'Positivo', 'Negativo'): 'Enterobacter aerogenes',
    ('Negativo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Positivo'): 'Enterobacter doawe',
    ('Positivo', 'Negativo', 'Negativo', 'Negativo', 'Positivo', 'Positivo', 'Positivo', 'Positivo'): 'Escherichia coli',
    ('Positivo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Positivo', 'Positivo'): 'Klebsiella oxytoca',
    ('Negativo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Positivo', 'Positivo'): 'Klebsiella pneumonia',
    ('Positivo', 'Negativo', 'Negativo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo'): 'Morganella morganii',
    ('Negativo', 'Positivo', 'Positivo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo'): 'Proteus mirabilis',
    ('Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Positivo'): 'Proteus vulgaris',
    ('Positivo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Negativo'): 'Providencia rettgeri',
    ('Positivo', 'Positivo', 'Negativo', 'Negativo', 'Negativo', 'Positivo', 'Positivo', 'Negativo'): 'Providencia stuartii',
    ('Negativo', 'Negativo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Negativo'): 'Salmonella Typhi',
    ('Negativo', 'Positivo', 'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Positivo'): 'Salmonella spp.',
    ('Negativo', 'Positivo', 'Negativo', 'Negativo', 'Positivo', 'Positivo', 'Positivo', 'Positivo'): 'Serratia marcescens',
    ('Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo'): 'Shigella sonnei',
    ('Positivo', 'Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo', 'Negativo'): 'Shigella spp.'
}

# Resultado
if st.button("Identificar Bactéria"):
    especie = tabela_identificacao.get(dados, "Nenhuma correspondência encontrada.")
    st.success(f"Resultado: {especie}")
    print("Ferramenta em desenvolvimento por Priscila Alencar - Microbiologista")
