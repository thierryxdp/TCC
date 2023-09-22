def repetidos(lista):
    '''Essa função recebe uma lista de números e retorna a quantidade
    de vezes que esse número é igual ao numero anterior, list->int'''
    n=0
    soma=0
    while n<len(lista)-1:
        if lista[n+1]==lista[n]:
           soma+=1
        n+=1
    return soma