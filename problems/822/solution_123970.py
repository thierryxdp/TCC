def repetidos(lista):
    """ Função que retorna quantos números repetidos tem
       int->list"""
    i = 1
    cont = 0
    while i < len(lista):
        if i == lista[i-1]:
                cont = cont+1
        i = i+1
    return cont