from django.db import models


class Image(models.Model):

    image = models.ImageField(
        "Carregar imagem"
    )

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"


class Interest(models.Model):

    description = models.CharField(
        "Interesse",
        max_length=50
    )

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"


class Student(models.Model):

    KNOWLEDGE_LEVEL = [
        ('0', 'Desconhece'),
        ('1', 'Básico'),
        ('2', 'Intermediário'),
        ('3', 'Avançado'),
    ]

    name = models.CharField(
        "Nome do aluno",
        max_length=80
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        verbose_name="Imagem"
    )
    knowledge_level = models.CharField(
        max_length=1,
        choices=KNOWLEDGE_LEVEL
    )
    interests = models.ManyToManyField(
        Interest,
        verbose_name="Interesses",
        related_name="student_interest"
    )
    created_at = models.DateTimeField(
        "Criado em",
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        "Atualizado em",
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.name
