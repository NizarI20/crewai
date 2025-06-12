from crewai import Crew
from content_agents import planner, writer, editor
from content_tasks import plan, write, edit

# Demander à l'utilisateur de saisir le sujet
topic = input("Entrez le sujet à traiter : ")

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=True
)


result = crew.kickoff(inputs={"topic": topic})

print(result.raw)  # Affiche la sortie finale de l'éditeur
# Sauvegarde dans report.md
with open("report.md", "w", encoding="utf-8") as f:
    f.write(result.raw)