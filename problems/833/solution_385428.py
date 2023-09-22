def conta_numero(numero,matriz):
    '''Recebe um número e uma matriz em forma de lista
    e retorna a quantidade de vezes que o número aparece
    na lista
    int,list->int'''
    qtd_num=0
    for i in matriz:
        for j in i:
            if numero == j:
                qtd_num=qtd_num+1
    return qtd_num