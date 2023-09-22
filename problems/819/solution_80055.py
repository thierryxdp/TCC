def filtraMultiplos(lista,n):
    """função que recebe uma lista de numeros e 
    um numero e retorna uma lista com apenas o numeros da lista que 
    são múltiplos ao numero n:list,int->list"""
    i=0
    resposta=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(resposta,lista[i])
        i=i+1
    return resposta