def primo(numero):
    contador=0
    for elemento in range(1,numero+1):
        if numero%elemento==0:
            contador=contador+1
    if contador<=2:
        return True
    else:
        return False