def maiores(lista_num,n):
    """ dada uma lista e um numero inteiro, vamos retornar uma nova lista que
        contenham somente os numeros maiores que N.
        Entrada --> list, int
        saida   --> list  """
    lista_num.append(n+1)
    lista_num.sort()
    posicao = lista_num.index(n+1)
    return lista_num[posicao+1:]


"""TESTE
Resultados esperados:
Resultados obtidos:
>>> maiores([1,2,3,4,5,3,7,8,9],6)
    [7, 8, 9]
"""