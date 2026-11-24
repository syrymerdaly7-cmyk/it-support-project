from django.db import models

class Ticket(models.Model):
    title = models.CharField("Тақырып", max_length=200)
    description = models.TextField("Сипаттама")
    priority = models.CharField("Басымдық", max_length=50, default="Орташа")
    status = models.CharField("Мәртебе", max_length=50, default="Жаңа")

    def __str__(self):
        return self.title
