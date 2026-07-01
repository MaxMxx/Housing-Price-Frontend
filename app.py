import pandas as pd
import requests
import streamlit as st

DEFAULT_BACKEND_URL = "https://fictional-giggle-4gvg7q977q73j4r-8000.app.github.dev"

st.set_page_config(
    page_title="California Housing Price Predictor",
    layout="centered",
)

with st.sidebar:
    st.header("Configuration")
    backend_url = st.text_input("URL du backend (FastAPI)", value=DEFAULT_BACKEND_URL)
    st.caption("URL de l'API déployée sur GitHub Codespaces (ex: https://xxxx-8000.app.github.dev).")
    st.divider()
    st.caption("Housing-Price-Frontend · Streamlit UI pour l'API California Housing.")

st.title("California Housing Price Predictor")
st.caption("Estimez la valeur médiane d'un logement à partir de ses caractéristiques.")

st.subheader("Revenu & logement")
col1, col2 = st.columns(2)
with col1:
    med_inc = st.number_input("MedInc — revenu médian (x 10k $)", value=8.3, format="%.4f")
    house_age = st.number_input("HouseAge — âge moyen des logements", value=41.0, format="%.4f")
with col2:
    ave_rooms = st.number_input("AveRooms — nb moyen de pièces", value=6.9, format="%.4f")
    ave_bedrms = st.number_input("AveBedrms — nb moyen de chambres", value=1.0, format="%.4f")

st.subheader("Quartier")
col3, col4 = st.columns(2)
with col3:
    population = st.number_input("Population du quartier", value=322.0, format="%.4f")
    ave_occup = st.number_input("AveOccup — occupation moyenne", value=2.5, format="%.4f")
with col4:
    latitude = st.number_input("Latitude", value=37.88, format="%.4f")
    longitude = st.number_input("Longitude", value=-122.23, format="%.4f")

st.map(pd.DataFrame({"lat": [latitude], "lon": [longitude]}), zoom=8, size=200)

predict_clicked = st.button("Predict", type="primary", use_container_width=True)

if predict_clicked:
    payload = {
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude,
    }

    if not backend_url:
        st.error("Merci de renseigner l'URL du backend dans la barre latérale.")
    else:
        with st.spinner("Appel du modèle en cours..."):
            try:
                response = requests.post(f"{backend_url.rstrip('/')}/predict", json=payload, timeout=30)
                response.raise_for_status()
                result = response.json()
                st.metric(
                    "Valeur médiane prédite (x 100k $)",
                    f"{result['predicted_house_value']:.2f}",
                )
                st.success("Prédiction récupérée avec succès.")
            except requests.exceptions.RequestException as e:
                st.error(f"Erreur lors de l'appel au backend : {e}")
