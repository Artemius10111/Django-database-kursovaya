from django.shortcuts import render, redirect
from .models import Client, NotariusService
from .forms import NotariusServiceForm

def notarius_service_list(request):
    services = NotariusService.objects.all()
    return render(request, 'notarius_service_list.html', {'services': services})

def client_form_view(request):
    if request.method == 'POST':
        form = NotariusServiceForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            # Используем get_or_create для получения или создания клиента
            client, created = Client.objects.get_or_create(result_name=first_name + ' ' + second_name, first_name=first_name, second_name=second_name)

            # Используем get_or_create для получения или создания услуги
            notarius_service, created = NotariusService.objects.get_or_create(title=title)


            # Если услуга уже существует, добавляем клиента в связь ManyToMany
            notarius_service.clients.add(client)

            notarius_service.description = description
            notarius_service.save()
            
            return redirect('notarius_service_list')
    else:
        form = NotariusServiceForm()

    return render(request, 'client_form.html', {'form': form})

# Инструкция для views 1
# При получении POST-запроса обработка формы происходит следующим образом:
# 1. Извлекаем данные из формы.
# 2. Используем метод get_or_create для получения или создания клиента по параметру "resultName".
# 3. Используем метод get_or_create для получения или создания услуги.
# 4. Если услуга уже существует, добавляем клиента в связь ManyToMany.
# 5. Перенаправляем пользователя на страницу с формой.

# Важно: В шаблоне 'client_form.html' необходимо создать форму для ввода данных и кнопку submit.