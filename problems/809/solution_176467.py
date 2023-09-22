def intercala(lista1, lista2):
    """ Dadas duas listas (lista1 e lista2) de tamanho 3, retorna uma lista que é o resultado de intercalar os elementos da lista1 e lista2 
    list, list -> list """
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]