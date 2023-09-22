def primo(numero):
    contador=numero-1
    while contador>1:
        contador=contador-1
        if numero%numero==0 and numero%1==0 and numero%contador!=0:
            resultado=True
        else:
            resultado=False
    return resultado