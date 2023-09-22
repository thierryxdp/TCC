def repetidos(lista_num):
    i = 0
    nova_lista = []
    quant = len(nova_lista)
    while i <= len(lista_num):
        if lista_num[i] == lista_num[i-1]:
            nova_lista.append(i)
            i += 1
        return quant