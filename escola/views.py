from rest_framework import viewsets, generics, authentication, permissions
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosCursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Lista alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

class CursosViewSet(viewsets.ModelViewSet):
    """Lista cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Lista matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

class ListaMatriculasAluno(generics.ListAPIView):
    """Lista matriculas de aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

class ListaAlunosMatriculadosCurso(generics.ListAPIView):
    """Lista alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCursoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
