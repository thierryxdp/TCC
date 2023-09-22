def repetidos(lista):
    """funcao que recebe uma lista, conta e retorna quantas 
    vezes um numero é igual ao anterior.
    entrada->list
    saida->int"""
   
    i=0
    vezes=[]
    while i<len(lista):
        if lista[i]==lista[i-1]:
            vezes=vezes+[1]
        i=i+1
    return len(vezes)