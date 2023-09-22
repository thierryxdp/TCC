def insere(lista_numero,n):
    """essa função dada uma lista ordenada (crescente) de números inteiros (igual ao
parâmetro de entrada lista_numero) e um número inteiro n, inclui n na posição correta, ou
seja, de tal maneira que a lista continua ordenada.
list,int -> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero