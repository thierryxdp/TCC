def primo(numero):
    lista_num_divisores= list(range(2,numero))
    resultado=0
    for indice in lista_num_divisores:
        while (numero%indice)!=0:
            resultado= True
        return resultado
        resultado= False
    return resultado