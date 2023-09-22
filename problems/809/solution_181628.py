def intercala(lista1, lista2):
    '''funcao que cria uma lista 3 formaada pelo os elementos da lista1 e lista2
       :param lista1: list->list
       :param lista2: list->list
       :return: list
       '''
     lista3= lista1+ lista2
     lista3[:2]=lista1
     lista3[1::2]=lista2     
      return lista3