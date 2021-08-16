from django.db import models
from django.utils.html import mark_safe


class Image(models.Model):

    image = models.ImageField(
        "Carregar imagem"
    )

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self):
        return self.image.url

    def image_tag(self):
        return mark_safe(
            f'<img src="{self.image.url}" width="80"/>'
        )

    image_tag.allow_tags = True


class Interest(models.Model):

    description = models.CharField(
        "Interesse",
        max_length=50
    )

    class Meta:
        ordering = ("description",)
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"

    def __str__(self):
        return self.description


class EventParticipant(models.Model):

    KNOWLEDGE_LEVEL = [
        ('Nenhum', 'Nenhum'),
        ('Básico', 'Básico'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado'),
    ]

    name = models.CharField(
        "Nome do Participante",
        max_length=80
    )
    email = models.EmailField(
        verbose_name="Email",
        null=True,
        blank=True
    )
    company = models.CharField(
        "Organização/Projeto",
        max_length=100,
        null=True,
        blank=True
    )
    join = models.BooleanField(
        default=False,
        verbose_name="Colaborador Join?"
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        verbose_name="Imagem"
    )
    knowledge_level = models.CharField(
        max_length=15,
        choices=KNOWLEDGE_LEVEL
    )
    interests = models.ManyToManyField(
        Interest,
        verbose_name="Interesses",
        related_name="participant_interest"
    )
    other_interest = models.CharField(
        "Outros interesses",
        max_length=15,
        null=True,
        blank=True
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
        unique_together = ["email"]
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"

    def __str__(self):
        return self.name
