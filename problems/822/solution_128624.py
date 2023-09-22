def repetidos(lista):
    """Retorna o número de vezes que tal elemento na lista é igual ao seu antecessor.
    list->int"""
    c=0
    f=0
    while c<len(lista):
        if lista[c-1]==lista[c]:
            f+=1
        c=c+1
    return f