from django.db import models


class Hub(models.Model):
    title = models.CharField(unique=True, db_index=True, verbose_name="Заголовок")
    hub_link = models.CharField(verbose_name="Ссылка на хаб", unique=True, db_index=True)

    class Meta:
        db_table: str = "hub"
        verbose_name: str = "Хаб"
        verbose_name_plural: str = "Хабы"

    def __str__(self):
        return self.title
