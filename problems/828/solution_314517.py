def primo(numero):
    resultado=0
    for indice in range(1,numero+1):
        if (numero%indice)!=0:
            resultado= True
        elif (numero%1)==0 and (numero%numero)==0:
            return True
        else:
            resultado= False
    return resultado