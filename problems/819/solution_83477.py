def filtraMultiplos(lis,n):
    '''
    Funçao que recebe um numero e um lista e filtra os numeros da lista 
    que sao divisiveis por n
    float, lis -> lis
    '''
    
    i=0
    l2=[]
    while i < len(lis):
        if lis[i]%n == 0:
            l2= l2+ lis(i)
    	i= i + 1
    return l2