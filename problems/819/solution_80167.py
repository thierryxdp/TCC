def filtraMultiplos(lista,n):
    """foda-se"""
    mul= []
    i=0
    while (i<len(lista)):
        if  int(lista[i])%n==0:
            mul= mul+ [int(lista[i])]
            i=i+1
        if  int(lista[i])%n!=0:
            mul= mul
            i=i+1
    
    return mul