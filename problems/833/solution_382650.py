def conta_numero(numero,matriz):
    '''Essa função conta e retorna quantas vezes um número aparece na matriz,
    int,list->int'''
    contador = 0
    for linha in matriz:
        for i in linha:
            if i == numero:
                contador+=1
    return contador