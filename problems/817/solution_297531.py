def acima_da_media(lista):
    '''
    Dado uma lista de notas, ordena as notas que ficaram acima da média.

    Uso:
    acima_da_media(lista)

    Entrada:
    - lista (list, int): Lista original

    Saída:
    - Retorna uma nova lista que contem as notas acima da média ordenadas. (lista)
    '''

    a= sum(lista)/len(lista)
    b=([i for i in lista if i > a])
    return sorted(b)