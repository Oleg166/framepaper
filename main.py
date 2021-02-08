from framepaper import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contacts/': views.contacts_view,
}


def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'SECRET'


def contacts_controller(request):
    request['contacts_list'] = 'ООО "Кто-то" г. Москва ул. Москрвская тел.: 8-800-999-9999'


front_controllers = [
    secret_controller,
    contacts_controller
]

application = Application(urlpatterns, front_controllers)

# Запуск:
# gunicorn main:application
