import streamlit as st
from crewai import Crew
from content_agents import planner, writer, editor
from content_tasks import plan, write, edit

st.title("Générateur de contenu CrewAI avec Llama 3 (Ollama)")
st.write(
    """
    Entrez un sujet pour générer un article complet (planning, rédaction, édition) en utilisant vos agents CrewAI et Llama 3.
    """
)

# Saisie utilisateur
topic = st.text_input("Sujet de l'article", "")

if st.button("Générer l'article"):
    if topic.strip():
        with st.spinner("Génération en cours..."):
            # Initialisation de l'équipe CrewAI
            crew = Crew(
                agents=[planner, writer, editor],
                tasks=[plan, write, edit],
                verbose=True
            )
            # Lancement de la génération
            result = crew.kickoff(inputs={"topic": topic})
            # Affichage du résultat
            st.success("Article généré !")
            st.markdown(result.raw)
            # Sauvegarde du résultat
            with open("report.md", "w", encoding="utf-8") as f:
                f.write(result.raw)
            # Proposer le téléchargement
            st.download_button("Télécharger le markdown", result.raw, "report.md")
    else:
        st.warning("Merci d'indiquer un sujet avant de lancer la génération.")