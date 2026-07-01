import requests
import streamlit as st

DEFAULT_BACKEND_URL = "https://fictional-giggle-4gvg7q977q73j4r-8000.app.github.dev"

st.set_page_config(page_title="Housing Price Prediction", page_icon="🏠")

st.title("🏠 Housing Price Prediction")
st.write(
    "Renseignez les caractéristiques du logement puis cliquez sur **Predict** "
    "pour obtenir la valeur médiane estimée (California Housing)."
)

backend_url = st.text_input("URL du backend (FastAPI)", value=DEFAULT_BACKEND_URL)

st.subheader("Caractéristiques du logement")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        med_inc = st.number_input("MedInc (revenu médian, en dizaines de milliers $)", value=8.3, format="%.4f")
        house_age = st.number_input("HouseAge (âge moyen des logements)", value=41.0, format="%.4f")
        ave_rooms = st.number_input("AveRooms (nombre moyen de pièces)", value=6.9, format="%.4f")
        ave_bedrms = st.number_input("AveBedrms (nombre moyen de chambres)", value=1.0, format="%.4f")

    with col2:
        population = st.number_input("Population (du quartier)", value=322.0, format="%.4f")
        ave_occup = st.number_input("AveOccup (occupation moyenne)", value=2.5, format="%.4f")
        latitude = st.number_input("Latitude", value=37.88, format="%.4f")
        longitude = st.number_input("Longitude", value=-122.23, format="%.4f")

    submitted = st.form_submit_button("Predict")

if submitted:
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
        st.error("Merci de renseigner l'URL du backend.")
    else:
        try:
            response = requests.post(f"{backend_url.rstrip('/')}/predict", json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()
            st.success(f"Valeur médiane prédite : **{result['predicted_house_value']}** (en centaines de milliers $)")
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de l'appel au backend : {e}")
