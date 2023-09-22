'''Função que dado duas listas lista1 e lista2 de tamanho 3, gera uma
lista3 que é formada intercalando os elementos da lista1 e da lista2
list,list->list'''
def intercala(lista1, lista2):
    lista3 = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista3