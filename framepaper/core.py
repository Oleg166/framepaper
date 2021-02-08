def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    print(type(environ))
    print(environ)
    path = environ['PATH_INFO']
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index. Hello WORLD from a simple WSGI application!']
    elif path == '/abc/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'abc. Hello WORLD from a simple WSGI application!']
    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return [b'404 Error']

    # сначала в функцию start_response передаем код ответа и заголовки
    start_response('200 OK', [('Content-Type', 'text/html')])
    # возвращаем тело ответа в виде списка из bite
    return [b'Hello WORLD from a simple WSGI application!']
