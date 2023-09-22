def primo(numero):
    resultado=0
    for indice in range(2,numero+1):
        if (numero%indice)>0:
            resultado=True
        else:
            resultado=False
    return resultado