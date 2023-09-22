def insere(lista_numero, n):
    '''dada uma lista ordenada crescente(lista_numero) de numeros inteiros, adiciona o numero inteiro(n) nessa lista, de forma que continue ordenada em ordem crescente; list,int -> list'''
    A = lista_numero 
    a = [n]
    B = A + a
    list.sort(B)
    return B