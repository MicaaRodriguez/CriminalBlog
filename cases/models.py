from django.db import models

class Case(models.Model):

    CASE_TYPES = [
        ("serial", "Asesino serial"),
        ("homicide", "Homicidio"),
        ("missing", "Persona desaparecida"),
        ("fraud", "Fraude"),
        ("other", "Otro"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to="case_images", null=True, blank=True)

    case_type = models.CharField(max_length=50, choices=CASE_TYPES)

    event_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title