def conta_numero(numero,matriz):
    '''Essa função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz'''
    '''int,list->int'''
    qt=0
    for n in matriz:
        for i in n:
            if i == numero:
                qt+=1
    return qt