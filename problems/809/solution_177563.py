def intercala(lista1,lista2):
    '''Dados os valores das lista1 e lista2-->int, retorna a soma das listas de forma intercalada'''
    intercalada=[]
    for a,b in zip(lista1,lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada

lista1 = [1,2,3]
lista2 = [4,5,6]

listaIntercalada=intercala(lista1, lista2)