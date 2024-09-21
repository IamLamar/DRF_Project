from django.db import models

class Todo(models.Model):
    author = models.CharField(max_length=100,verbose_name="Автор")
    title = models.CharField(max_length=100,verbose_name="Название")
    body = models.TextField(verbose_name="Содержание")

    def __str__(self) -> str:
        return  self.author
    
    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"


