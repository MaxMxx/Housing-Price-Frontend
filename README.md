# Housing-Price-Frontend

Frontend Streamlit pour l'API de prédiction du prix des logements (California Housing).

Communique avec le backend FastAPI Housing-Price déployé sur GitHub Codespaces.

## Lancer en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Déploiement sur Streamlit Community Cloud

1. Pousser ce repo sur GitHub.
2. Sur [streamlit.io](https://streamlit.io), créer une nouvelle app en pointant vers ce repo et le fichier `app.py`.
3. Une fois déployée, renseigner l'URL du backend Codespaces dans le champ prévu à cet effet sur la page.
