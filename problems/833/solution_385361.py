def conta_numero(numero,matriz):
    '''conta quantas vezes um certo numero aparece em uma matriz;
    int,list->int'''
    n_vezes=0
    for linha in matriz:
        for num in linha:
            if num==numero:
                n_vezes+=1
    return n_vezes