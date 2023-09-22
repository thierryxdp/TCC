def eh_quadrada(matriz):
    '''verifica se a matriz é quadrada
    list--> bool'''

    for item in matriz:
        for item2 in item:
            if item2 == list([]) or len(matriz) == len(item):
                return True
            else:
                return False