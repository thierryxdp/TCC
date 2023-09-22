def faltante(lista):
    completo=list(range(1,len(lista)+2))
    cont=0
    while cont<len(lista):
        if lista[cont] != completo[cont]:
            return completo[cont]
        cont+=1
    return completo[cont]