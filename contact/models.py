from django.db import models


class EmployerApplication(models.Model):
    email = models.EmailField("Email отправителя", max_length=255)

    class ProvisionKindChoices(models.TextChoices):
        WORK = 'w', 'Работу'
        WORK_AND_DWELLING = 'd', 'Работу и проживание'
        WORK_AND_FOOD = 'f', 'Работу и еду'
        ALL = 'a', 'Работу, еду и проживание'

        __empty__ = 'Выберите то, что можете предоставить'

    provision_kind = models.CharField("Обеспечение", max_length=1, choices=ProvisionKindChoices.choices, default=ProvisionKindChoices.__empty__)
    description = models.TextField("Описание деятельности", max_length=2000)
    comment = models.TextField("Комментарий отправителя", max_length=2000, blank=True)

    class Meta:
        verbose_name = "Заявка работодателя"
        verbose_name_plural = "Заявки работодателей"

    def __str__(self) -> str:
        return self.email


class TouristApplication(models.Model):
    email = models.EmailField("Email отправителя", max_length=255)
    health = models.TextField("Здоровье отправителя", max_length=2000)
    description = models.TextField("Описание отправителя", max_length=2000)
    comment = models.TextField("Комментарий отправителя", max_length=2000, blank=True)

    class Meta:
        verbose_name = "Заявка туриста"
        verbose_name_plural = "Заявки туристов"

    def __str__(self) -> str:
        return self.email 


class Collaboration(models.Model):
    title = models.CharField("Название сотрудничающей организации", max_length=100)
    short_description = models.TextField("Краткое описание организации", max_length=500)
    url = models.URLField("Ссылка на подробности организации", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Сотрудничающая организация"
        verbose_name_plural = "Сотрудничающие организации"

    def __str__(self) -> str:
        return self.title
