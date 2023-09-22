def eh_quadrada(matriz:list)->bool:
    'recebe uma matriz e identifica se ela é quadrada'
    for i in matriz:
        if len(matriz) != len(i):
            return False
        return True