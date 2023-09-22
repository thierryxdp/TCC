def primo(numero):
    '''função que retorna True se o número for primo e False
    caso não seja.
    int->bool'''
    lista_num_divisores= list(range(2,numero))
    lista_resto=[]
    for indice in lista_num_divisores:
        resto= numero%indice
        list.append(lista_resto,resto)
    if 0 in lista_resto:
        return False
    else:
        return True