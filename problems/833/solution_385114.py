def conta_numero (n,matriz):
    '''Retorna quantas vezes o número n aparece na matriz;
    int,list->int'''
    qtd_n = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == n:
                qtd_n += 1
    return qtd_n