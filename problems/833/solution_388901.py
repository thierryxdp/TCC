def conta_numero(numero,matriz):
    "Verifica a incidência de um número em uma matriz. int, list --> int"
    cont_num = 0
    for j in matriz:
        for x in j:
            if numero == x:
                cont_num += 1
    return cont_num