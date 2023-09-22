def  repetidos(lista_num):
    '''função   que  conta  quantas  vezes  um  numero
     apareceu  repetido'''
    'list--> int'
    i = 1
    qtd =  0

    while  len(lista_num)  >  i:
        if lista_num[i] == lista_num[i - 1]:
            qtd += 1
            i += 1
        else:
            i += 1
            return qtd