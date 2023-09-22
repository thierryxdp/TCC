def intercala(lista1, lista2):
   '''funcao que cria uma lista 3 formada pelo os elementos da lista1 e lista2
   :param lista1: list->1,3,5
   :param lista2: list->2,4,6
   :return: list
   '''
    lista3= lista1+ lista2
    lista3[::2]=lista1
    lista3[1::2]=lista2
   return lista3