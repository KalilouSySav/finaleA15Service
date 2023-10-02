from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from finaleA15Service.services import ProjectService

project_service = ProjectService()


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def insert_project_data(request):
    code_projet = request.POST.get('code_projet')
    description = request.POST.get('description')
    if code_projet is None or description is None:
        return JsonResponse({'status': 'error', 'message': 'Missing parameters'})
    project_service.insert_project_data(code_projet, description)
    return JsonResponse({'status': 'success'})


def get_project_data(request, project_id):
    project_data = project_service.get_project_data(project_id)
    return JsonResponse(project_data)


def accueil(request):
    return render(request, 'index.html')