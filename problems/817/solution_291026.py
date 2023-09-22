def insere(lista_numero, n):
    """Recebe uma lista ordenada de números e um número qualquer, e retorna o
    a lista com o número inserido na sequência ordenada"""
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero, n):
    """Recebe uma lista de números inteiros e um número n também inteiro.
    Retorna uma sublista de números maiores que o número n contidos na lista"""
    lista_numero = insere(lista_numero, n)
    indice = list.index(lista_numero, n)
    lista_nova = lista_numero[indice+1:]
    return lista_nova

def acima_da_media(lista_notas):
    """Recebe uma lista com as notas de uma turma e retorna as notas que ficaram
    acima da média em uma nova lista"""
    media = sum(lista_notas)/len(lista_notas)
    if media in lista_notas:
        list.remove(lista_notas, media)
    aprovados = maiores(lista_notas, media)
    return aprovados