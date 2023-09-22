def qtd_divisores(n):
    """Conta quantos divisores naturais 
    o número n tem
    int-->int"""
    div=[]
    for N in range (1,n+1):
        if n%N==0:
            list.append(divisores,N)
    return len(div)