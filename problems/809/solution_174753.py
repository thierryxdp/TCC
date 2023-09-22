'''Recebe duas listas de tamanho 3 e junta intercalando na lista 3'''
def intercala(lista1,lista2):
    lista3 = [] #Abre uma lista vázia para preencher
    for x,y in zip(lista1, lista2): # Junta as duas listas colocando um certo x da lista 1 e y da lista 2 na lista 3
        lista3.append(x)
        lista3.append(y)
    return lista3