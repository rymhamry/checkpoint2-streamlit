import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

def app():
    st.subheader("Exploration des données financières")

    # Vérifie si les données sont chargées
    if 'data' not in st.session_state:
        st.error("Aucune donnée disponible. Veuillez d'abord téléverser un fichier CSV dans la page principale.")
        return

    df = st.session_state['data']

    st.write("Aperçu des données :")
    st.write(df.head())

    st.write("### Statistiques descriptives")
    st.write(df.describe())

    # Corrélation
    if st.checkbox("Afficher la matrice de corrélation"):
        corr = df.corr(numeric_only=True)
        fig = px.imshow(corr, text_auto=True, title="Matrice de corrélation")
        st.plotly_chart(fig)

    # Visualisation Scatter
    st.write("### Visualisation : Nuage de points")
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) >= 2:
        x_col = st.selectbox("X-axis", num_cols)
        y_col = st.selectbox("Y-axis", [col for col in num_cols if col != x_col])
        fig_scatter = px.scatter(df, x=x_col, y=y_col, title="Scatter Plot")
        st.plotly_chart(fig_scatter)
    else:
        st.warning("Pas assez de colonnes numériques.")

    # Histogramme
    st.write("### Distribution des données")
    column = st.selectbox("Choisissez une colonne", num_cols)
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=20, color="skyblue", edgecolor="black")
    ax.set_title(f"Histogramme de {column}")
    st.pyplot(fig)
