def insere(lista_numero,n):
    ''' funcao que dada uma lista ordenada (crescente) de numeros inteiros e um numero inteiro n inclua n na posicao correta;
list , int -> list '''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return (lista_numero1 - insere(lista_numero,n))