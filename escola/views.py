from rest_framework import viewsets, generics, status
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosCursoSerializer
from rest_framework.response import Response

class AlunosViewSet(viewsets.ModelViewSet):
    """Lista alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Lista cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response['Location'] = request.build_absolute_uri() + id
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatriculasViewSet(viewsets.ModelViewSet):
    """Lista matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class ListaMatriculasAluno(generics.ListAPIView):
    """Lista matriculas de aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculadosCurso(generics.ListAPIView):
    """Lista alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCursoSerializer
