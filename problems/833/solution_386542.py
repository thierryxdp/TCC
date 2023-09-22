def conta_numero(numero,matriz):
    '''Recebe um número inteiro e uma matriz e retorna quantas vezes o número aparece na matriz; float,list->int'''
    total=0
    for linha in matriz:
        for coluna in linha:
            if coluna==numero:
                total=total+1
    return total