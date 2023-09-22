def conta_numero(numero,matriz):
    """essa função retorna quantas vezes um determinado número aparece na matriz;
    int,list-->int"""
    cont = 0
    for x in matriz:
        for num in x:
            if numero == num:
                cont = cont + 1
    return cont