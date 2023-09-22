def filtraMultiplos(lista,n): 
    '''funçao que retorna uma lista com os números múltiplos de n de entrada''' 
    '''list,int->list'''
    multiplos=[]
    i=0
    while i < len(lista):
        if lista[i]%n ==0:
            list.append(multiplos,lista[i])
        i=i+1 
    return multiplos