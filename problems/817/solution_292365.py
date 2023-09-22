def maiores(lista, n):
    """Função que dada uma lista de números inteiros e um número inteiro n, retorna uma nova lista
    contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    int, int -> int """
    
    list(lista)
    lista.append(n)
    lista_nov = sorted(lista)
    indN = lista_nov.index(n)
    if n not in lista_nov:
        lista.append(n)

    return lista_nov[indN + 1:]

from math import floor

def acima_da_media(lista):
    
    """ Função que dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    list -> list """
    
    media = int(sum(lista) / len(lista))
    lista.append(media)
    lista_nov= sorted(lista)
    indM = lista_nov.index(media)
    novaLista = lista_nov[indM + 1:].copy()

    if media in lista2:
        del lista2[0]

   	return lista2