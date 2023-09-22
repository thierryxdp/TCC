def filtraMultiplos(lis,n):
    '''
    Funçao que recebe um numero e um lista e filtra os numeros da lista 
    que sao divisiveis por n
    float, lis -> lis
    '''
    
    i=0
    L=[]
    while i < len(lis):
        if lis[i]%n == 0:
            L= L + lis[i]
    	i= i + 1
    return L