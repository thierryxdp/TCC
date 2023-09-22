def acima_da_media(lista):
    '''Recebe uma lista com as notas dos alunos e 
    retorna uma lista ordenada com as notas que ficaram 
    acima da média.
    list -> list'''
    acima = []
    media = sum(lista) / len(lista)
    numeros = tuple(lista)
    if numeros > media:
        acima += lista
        return acima