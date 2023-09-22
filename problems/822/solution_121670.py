def repetidos(lista):

    repetidos=[]
    proximo=0

    while proximo<len(lista):
        if lista[proximo]==lista[proximo-1]:
            repetidos=repetidos+[lista[proximo],]
            proximo=proximo+1
        else:
            proximo=proximo+1

    return len(repetidos)