from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from ckeditor.fields import RichTextField


class Case(models.Model):

    CASE_TYPES = [
        ("serial", "Asesino serial"),
        ("homicide", "Homicidio"),
        ("missing", "Persona desaparecida"),
        ("fraud", "Fraude"),
        ("other", "Otro"),
    ]

    title = models.CharField(max_length=200)

    # CKEDITOR
    description = RichTextField()

    image = models.ImageField(upload_to="case_images", null=True, blank=True)

    case_type = models.CharField(max_length=50, choices=CASE_TYPES)

    event_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """
        Evita que se creen casos con fechas futuras
        """
        if self.event_date > timezone.now().date():
            raise ValidationError({
                "event_date": "La fecha del caso no puede ser posterior a la fecha actual."
            })

    def __str__(self):
        return self.title