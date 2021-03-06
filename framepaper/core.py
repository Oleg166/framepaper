class Application:

    def add_route(self, url):
        # паттерн декоратор
        def inner(view):
            self.urlpatterns[url] = view

        return inner

    def parse_accept_data(self, data: str):
        result = {}
        if data:
            items = data.split('&')

            for item in items:
                b, c = item.split('=')
                result[b] = c
        return result

    def parse_wsgi_accept_data(self, data: bytes):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_accept_data(data_str)
        return result

    def get_wsgi_accept_data(self, env):
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def __init__(self, urlpatterns: dict, front_controllers: list):
        """
        :param urlpatterns: словарь связок url: view
        :param front_controllers: список front controllers
        """
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        # текущий url
        path = env['PATH_INFO']

        # добавление закрывающего слеша
        if not path.endswith('/'):
            path = f'{path}/'

        # Получаем все данные запроса
        method = env['REQUEST_METHOD']
        data = self.get_wsgi_accept_data(env)
        data = self.parse_wsgi_accept_data(data)

        query_string = env['QUERY_STRING']
        request_params = self.parse_accept_data(query_string)

        if path in self.urlpatterns:
            # получаем view по url
            view = self.urlpatterns[path]
            request = {}
            # добавляем параметры запросов
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params
            # добавляем в запрос данные из front controllers
            for controller in self.front_controllers:
                controller(request)
            # вызываем view, получаем результат
            code, text = view(request)
            # возвращаем заголовки
            start_response(code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # Если url нет в urlpatterns - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]
