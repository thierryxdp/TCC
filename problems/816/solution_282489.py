def insere (lista_numero, n):
    '''dada uma lista ordenada(crescente) de numeros inteiros e um numero inteiro, retorna uma lista com o numero inteiro na
       posiçao correta.
       : list, int -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

def maiores (lista_numeros, n):
    '''dada uma lista de numeros inteiros e um numero inteiro, retorna uma lista que contenha todos os números da lista 
       original maiores que o numero dado, ordenados em ordem crescente
       : list, int -> list
    '''
    lis_ord = insere(lista_numeros, n)
    n_maior = lis_ord[n+1:]
    return n_maior