def insere(lista_numero,n):
    """dada uma lista ordenada de núemros inteiros e um número inteiro n, 
a função insere n na lista de forma que ela continue ordenada.
list, int--> list

Parâmetros
lista_numero: lista ordenada utilizada como entrada
n: número inteiro a ser adicionada à lista"""
    y=list.append(lista_numero,n)
    x=list.sort(lista_numero)
    return lista_numero