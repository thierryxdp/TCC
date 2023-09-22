def insere(lista,n):
    """recebe uma lista e um número inteiro n e retorna a mesma lista acrescentado n, em ordem crescente.
    list,int->list""" 
    lista.append(n)
    lista.sort()
    return lista