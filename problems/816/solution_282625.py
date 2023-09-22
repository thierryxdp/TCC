def insere (lista_numero, n):
    '''dada uma lista ordenada(crescente) de numeros inteiros e um numero inteiro, retorna uma lista com o numero inteiro na
       posiçao correta.
       : list, int -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

def maiores (lista_numero, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna uma lista que contenha todos os números da lista 
       original maiores que n, em ordem crescente.
    '''
    copia = lista_numero.copy()
    insere = copia.append(n)
    ordena = insere.sort()
    indice = ordena.index(n)
    n_lista = indice[indice+1:]
    return n_lista