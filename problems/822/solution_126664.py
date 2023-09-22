def repetidos(numeros):
    """retorna a quantidade de vezes que um numero é igual ao seu
    sucessor numa lista. (list->int)"""
    duplas=0
    i=1
    while i<len(numeros):
        if numeros[i]==numeros[i-1]:
            duplas+=1
            i+=1
        else:
            i+=1
    return duplas