def faltante(lista):
    """ recebe um lista e descobre qual valor está faltando na sequência;lista->int"""
    parametro=lista[-1]
    lista2=list(range(1,parametro))
    indice=0
    lista3=[]
    lista4= lista[-1] + 1
    while(indice<len(lista)):
        if lista2[indice] not in lista:
            list.append(lista3,lista2[indice])
        else:
            list.append(lista3,lista4)
        indice+=1
    return lista3[0]