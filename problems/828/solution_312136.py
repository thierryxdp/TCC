def primo(n):
    divisores=[]
    for numero in range(1,n+1):
        if n%numero==0:
            list.append(divisores,numero)
    return len(divisores)==2