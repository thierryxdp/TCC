def intercala(lista1,lista2):
    ''' Recebe duas listas e retorna uma terceira lista intercalando os itens das listas 1 e 2'''
    lista3 = []
    for i in range(3):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3