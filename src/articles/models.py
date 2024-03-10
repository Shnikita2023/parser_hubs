from django.db import models


class Article(models.Model):
    title = models.CharField(unique=True, db_index=True, verbose_name="Заголовок")
    date = models.CharField(verbose_name="Дата публикации")
    author_name = models.CharField(verbose_name="Имя автора")
    content = models.TextField(verbose_name="Текст статьи")
    author_link = models.CharField(verbose_name="Ссылка на автора")
    article_link = models.CharField(verbose_name="Ссылка на статью", unique=True, db_index=True)

    hub = models.ForeignKey(to="hubs.Hub",
                            on_delete=models.CASCADE,
                            verbose_name="Идентификатор хаба",
                            related_name="articles")

    class Meta:
        db_table: str = "article"
        verbose_name: str = "Статья"
        verbose_name_plural: str = "Статьи"

    def __str__(self):
        return self.title
