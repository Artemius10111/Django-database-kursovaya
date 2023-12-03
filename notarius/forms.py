# forms.py
from django import forms
from django.utils.translation import gettext as _

class NotariusServiceForm(forms.Form):
    first_name = forms.CharField(label=_("Имя"), max_length=255)
    second_name = forms.CharField(label=_("Фамилия"), max_length=255)
    title = forms.CharField(label=_("Название"), max_length=255)
    description = forms.CharField(label=_("Описание"), widget=forms.Textarea)

# Инструкция для формы
# Форма NotariusServiceForm содержит поля для ввода имени (first_name), фамилии (second_name),
# названия (title) и описания (description). Для создания услуги на странице необходимо
# ввести данные в эти поля и нажать кнопку submit. Затем будет использован метод get_or_create
# для получения клиента по параметру "resultName" и добавления клиента в поле clients,
# если NotariusService уже существует.
