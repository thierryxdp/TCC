# Essa função cria uma lista que intercala os valores dessas duas listas
def intercala(lista1, lista2):
    #L1 , L2 -> L3 
    # lista3 cria lista vazia
    lista3= []
    lista3 = lista3 + [lista1[0],]
    lista3 = lista3 + [lista2[0],]
    lista3 = lista3 + [lista1[1],]
    lista3 = lista3 + [lista2[1],]
    lista3 = lista3 + [lista1[2],]
    lista3 = lista3 + [lista2[2],]
    return lista3