def insere(lista_numero, n):
    """Dada uma lista ordenada (crescente) de números inteiros e um número
inteiro n, o procedimento deverá retornar a lista ordenada com n na posição
correta.
Assinatura: list, int -> list
Casos de teste:
insere([1,4,5,7,9,12], 3) == [1,3,4,5,7,9,12]
insere([2,3,6,8,9,15], 5) == [2,3,5,6,8,9,15]
"""
    lista = lista_numero
    list.append(lista, n)
    x = sorted(lista_numero)
    
    return x