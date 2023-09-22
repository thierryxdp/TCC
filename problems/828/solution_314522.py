def primo(numero):
    lista_num_divisores= list(range(2,numero))
    resultado=0
    for indice in lista_num_divisores:
        if (numero%indice)!=0:
            resultado= True
        else:
            resultado=False
    return resultado