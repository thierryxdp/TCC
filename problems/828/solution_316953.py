def primo(n):
    for i in range(2,n):
        if n%i==0 and i!=n:
            resultado = False
        else:
            resultado = True
    return resultado