def maiores(lista,num):
    lista_valida = filter(maiores,lista)
    if lista_valida > list(num):
        return lista_valida.append(num)
    else:
        return l