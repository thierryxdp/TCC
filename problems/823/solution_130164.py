def faltante(lista):
    list.sort(lista)
    tamanho=len(lista)-1
    todas=list(range(1,tamanho+2))
    elemento=0
    while elemento<len(lista):
        if lista[elemento]==todas[elemento]:
            return todas[elemento]
            elemento=elemento+1
        else:
   	return todas[elemento]