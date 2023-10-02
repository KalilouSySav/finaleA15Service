from typing import Dict, Any
from finaleA15Service.models import Project


class ProjectService:
    def insert_project_data(self, code: str, description: str) -> None:
        # Créez un nouvel objet de projet et enregistrez-le dans la base de données
        project = Project(code_projet=code, description=description)
        project.save()

    def get_project_data(self, project_id: int) -> Dict[str, Any]:
        try:
            # Récupérez les données du projet en fonction de l'ID du projet
            project = Project.objects.get(pk=project_id)
            project_data = {
                'code_projet': project.code_projet,
                'description': project.description
            }
            return project_data
        except Project.DoesNotExist:
            return {'error': 'Projet non trouvé'}
