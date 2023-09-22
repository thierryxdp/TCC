def intercala(lista1, lista2):
    """ Essa função intercala os termos de duas listas. """
    """ list, list ---> list. """
    
    #definindo os termos da lista1:
    termo1 = lista1[0]
    termo2 = lista1[1]
    termo3 = lista1[2]
        
    #definindo os termos da lista2:
    termo4 = lista2[0]
    termo5 = lista2[1]
    termo6 = lista2[2]
        
    #criando a lista 3:
    lista3 = [termo1, termo4, termo2, termo5, termo3, termo6]
        
    #retornando lista3:
    return (lista3)