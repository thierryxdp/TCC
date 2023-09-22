def primo(numero):
    resultado=0
    for indice in range(1,numero):
        if (numero%indice)!=0:
            resultado=True
        else:
            resultado=False
    return resultado