def qtd_divisores(n):
    """Conta quantos divisores naturais 
    o número n tem
    int-->int"""
    for N in range (1,n+1):
        divisores=[]
        if n%N==0:
            list.append(divisores,N)
    return len(divisores)