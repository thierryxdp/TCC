def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que um valor aparece numa matriz; int,list -> int'''
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contador = contador + 1
    return contador