def filtraMultiplos(lista,n):
    """foda-se"""
    mul= []
    i=0
    while (int(lista[i])%n==0):
        mul= mul+ [int(lista[i])]
        i= i +1