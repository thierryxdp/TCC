def faltante(lista):
    completo=range(1,len(lista)+1)
    cont=0
    while cont<len(lista):
        if lista[cont] in completo:
            list.remove(completo,lista[cont])
        cont+=1
    return completo