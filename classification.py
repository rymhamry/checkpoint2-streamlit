import streamlit as st
import pandas as pd
import joblib

def app():
    st.subheader("Modèle de classification")

    # Vérifie si les données sont chargées
    if 'data' not in st.session_state:
        st.error("Aucune donnée disponible. Veuillez d'abord téléverser un fichier CSV dans la page principale.")
        return

    df = st.session_state['data']

    # Vérifier si la colonne cible est présente
    if 'job_type' not in df.columns:
        st.warning("La colonne cible 'job_type' est manquante dans le dataset.")
        return

    try:
        model = joblib.load('model.pkl')
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {e}")
        return

    # Préparation des données
    X = df.drop('job_type', axis=1)
    y = df['job_type']

    # Prédictions
    st.write("### Résultats de la prédiction")
    try:
        prediction = model.predict(X)
        st.write(prediction)
    except Exception as e:
        st.error(f"Erreur pendant la prédiction : {e}")
