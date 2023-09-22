def faltante(lista):
    list.sort(lista)
    tamanho=len(lista)
    todas=list(range(1,tamanho+2))
    elemento=0
    elemento1=0
    while elemento<len(lista):
        if lista[elemento]==todas[elemento1]:
            elemento=elemento+1
            elemento1=elemento1+1
        else:
            
    return todas[elemento1]