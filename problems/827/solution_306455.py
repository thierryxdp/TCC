def qtd_divisores(numero):
    'função que dado um numero, retorna uma lista com todos seus divisores'
    lista_de_divisores=[]
    lista_de_possiveis_divisores=list(range(1,numero+1))
    for possivel_divisor in lista_de_possiveis_divisores:
        if numero%(possivel_divisor) == 0:
            list.append(lista_de_divisores,possivel_divisor)
    return lista_de_divisores