def primo(numero):
    lista_num_divisores= list(range(2,numero))
    lista_resto=[]
    resultado=0
    for indice in lista_num_divisores:
        resto= numero%indice
        list.append(lista_resto,resto)
    if 0 in lista_resto:
        return False
    else:
        return True