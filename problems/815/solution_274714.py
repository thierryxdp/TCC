def insere(lista_numero,n):
    """Função que dado uma lista ordenada de forma crescente e um número inteiro qualquer (n), retorna uma lista
ainda ordenada de forma crescente, porém, com o valor inteiro (n) inserido na lista.
list, int -> list
testes:
insere([1,2,17,19],10) == [1,2,10,17,19]
insere([10,20,30,40,60],50) == [10,20,30,40,50,60]
"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero