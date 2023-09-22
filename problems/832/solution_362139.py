def eh_quadrada(x):
    'devolve um valor booleano para a matriz. Se ela for quadradra renorna sim, caso contario retorna nao. list->valor booleano'
    if len(x) == len(x[0]):
        return print('sim')
    else:
        return print('não')