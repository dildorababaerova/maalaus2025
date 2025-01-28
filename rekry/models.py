from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)  # Название вакансии
    description = models.TextField()  # Описание вакансии
    requirements = models.TextField()  # Требования
    location = models.CharField(max_length=100)  # Локация
    created_at = models.DateTimeField(auto_now_add=True)  # Дата публикации

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')  # Связь с вакансией
    name = models.CharField(max_length=100)  # Имя кандидата
    email = models.EmailField()  # Email
    phone = models.CharField(max_length=20)  # Телефон
    resume = models.FileField(upload_to='resumes/')  # Резюме
    cover_letter = models.TextField(blank=True, null=True)  # Сопроводительное письмо
    submitted_at = models.DateTimeField(auto_now_add=True)  # Дата подачи

    def __str__(self):
        return f"{self.name} - {self.job.title}"


