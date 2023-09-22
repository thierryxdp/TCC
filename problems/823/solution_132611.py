def faltante (lista_num):
    """função que recebe um lista numérica qualquer (lista_num)
    e verifica qual número que está faltanto desse intervalo. E por
    fim retorna o número que falta <n>;
    lista->int"""
    i = 0
    list.sort(lista_num)
    n = lista_num[i]
    while n in lista_num:
        n = n + 1
        i=i+1
    return n