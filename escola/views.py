from django.http import JsonResponse

def alunos(req):
    if req.method == 'GET':
        aluno = {'id': 1, 'Nome': 'Exemplo'}
        return JsonResponse(aluno)
