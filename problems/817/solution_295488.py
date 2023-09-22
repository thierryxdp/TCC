def maiores(lista_numeros, n):
    '''Função que recebe um número inteiro e uma lista de 
    números inteiros, e retorna uma nova lista com os elementos
    maiores que o número n.
    [list] -> [list]'''
    if n in lista_numeros:
        lista_numeros = lista_numeros + [n]
        list.sort(lista_numeros)
        lista_final = lista_numeros[list.index(lista_numeros, n) + 2: ]
        return lista_final
    else:
        lista_numeros = lista_numeros + [n]
        list.sort(lista_numeros)
        lista_final = lista_numeros[list.index(lista_numeros, n) + 1: ]
        return lista_final
    
def acima_da_media(lista_notas):
    '''Função que recebe a lista de notas de uma turma
    e retorna uma lista ordenada das notas acima da média
    que a turma obteve.
    [list] -> [list]'''
    soma = sum(lista_notas)
    numero_de_notas = len(lista_notas)
    media = soma/numero_de_notas
    lista_final = maiores(lista_notas, media)
    return lista_final