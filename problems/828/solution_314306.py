def primo(n):
    """"""
    """"""
    contador=0
    numeros = list(range(2,n))
    for numero in numeros:
        if n%numero==0:
            contador=contador+1
    if contador == 0:
        return True
    else:
        return False