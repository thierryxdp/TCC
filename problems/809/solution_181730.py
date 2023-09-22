def intercala(lista1, lista2):
    '''Essa função, dada duas listas 1 2, retorna uma nova lista intercalando os elementos das listas 1 e 2, list,list -> list'''
    lista=[]
    lista3=[lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    for i in lista3:
        lista.append(i)
    return list(lista3)