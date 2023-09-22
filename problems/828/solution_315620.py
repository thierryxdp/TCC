def primo(n):
    """Recebe um número inteiro positivo, retorna se ele é primo
    int-->bool"""
    divisores=[]
    for N in range(1,n+1):
        if n%N==0:
            list.append(divisores,N)
    if len(divisores)==2:
        return True
    else:
        return False