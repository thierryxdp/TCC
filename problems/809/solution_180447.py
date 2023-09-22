def intercala(lista1, lista2):
    """Função que recebe duas listas de tamanho 3,
e gera uma terceira lista com os elementos intercalados
das duas primeiras.
assinatura: list, list --> list
casos de testes:
intercala([1,3,5],[2,4,6]) == [1, 2, 3, 4, 5, 6]
intercala([2,4,6],[3,5,7]) == [2, 3, 4, 5, 6, 7]
intercala([10,30,50],[20,40,60]) == [10, 20, 30, 40, 50, 60]
intercala([1,2,3],[100,200,300]) == [1, 100, 2, 200, 3, 300]
"""
    lista3 = ([lista1[0]]+ [lista2[0]] + [lista1[1]] +
              [lista2[1]] + [lista1[2]] + [lista2[2]])
    return lista3