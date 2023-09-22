def conta_numero(numero,matriz):
    ''' funcao que dado um numero retorna quantas vezes o mesmo aparece em uma matriz
    int,list->int'''
    contador = 0
    for linha in matriz:
        for i in linha:
            if i == numero:
                contador = contador + 1
    return contador