def intercala(lista1, lista2):
    '''Dadas duas listas, lista1 e lista2, de tamanho 3, gera uma lista 'lista3' que e formada
intercalando os elementos de lista1 e lista2. List,List-> List'''
    lista11 = lista1[:]
    lista22 = lista2[:]
    L3 = [lista11[0],lista22[0], lista11[1],lista22[1],lista11[2],lista22[2]]
    return L3