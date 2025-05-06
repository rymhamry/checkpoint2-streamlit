import streamlit as st
import pandas as pd
import financial, classification

st.set_page_config(page_title="Inclusion Financière", layout="wide")
st.title("Analyse de l'inclusion financière")

# --- Téléversement du fichier CSV ---
uploaded_file = st.file_uploader("Téléverser le fichier CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['data'] = df  # Stocker dans session_state
    st.success("Fichier chargé avec succès !")
    st.write(df.head())
else:
    st.warning("Veuillez téléverser un fichier CSV pour continuer.")
    st.stop()  # Empêche d'exécuter la suite si pas de données

# --- Navigation Sidebar ---
st.sidebar.title('Navigation')
page = st.sidebar.radio("Choisissez une page", ["Exploration Financière", "Classification"])

# --- Chargement des pages ---
if page == "Exploration Financière":
    financial.app()
elif page == "Classification":
    classification.app()
