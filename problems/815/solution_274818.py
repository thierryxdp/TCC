def insere(lista_numero,n):
    """Função que dada uma lista ordenada de forma crescente e um número inteiro qualquer (n), retorna uma lista
também ordenada de forma crescente, porém com o valor inteiro (n) inserido a lista.
assinatura: list, int -> list
testes:
insere([1,2,3,4],6) == [1, 2, 3, 4, 6]
insere([11,30,42,50,120],87) == [11, 30, 42, 50, 87, 120]
"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero