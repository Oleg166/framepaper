from framepaper import render


def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"


def contacts_view(request):
    contacts_list = request.get('contacts_list', None)
    return '200 OK', render('contacts.html', contacts_list_page=contacts_list)


def feedback_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        first_name = request['first_name']
        telephone = request['telephone']
        email = request['email']
        text = request['text']
        print(f'Нам пришло сообщение от {first_name} (тел.: {telephone}, e-mail: {email}) с текстом "{text}".')
        return '200 OK', render('feedback.html')
    else:
        return '200 OK', render('feedback.html')
