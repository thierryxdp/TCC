def intercala(lista1, lista2):
#list,list->list
    lista_conjunta = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista_conjunta
    """coloca os valores de cada lista de modo intercalado"""

#casos de teste
"""
intercala([1,2,3],[4,5,6]) == [1, 4, 2, 5, 3, 6]
intercala(["um","três","cinco"],["dois","quatro","seis"]) == ['um', 'dois', 'três', 'quatro', 'cinco', 'seis'] 
"""