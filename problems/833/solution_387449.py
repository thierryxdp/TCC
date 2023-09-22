def conta_numero(numero,matriz):
    """dado um int numero de entrada, e uma matriz de inteiros
    em forma de lista, conta e retorna quantas vezes numero
    aparece em matriz"""
    ocorrencias=0
    for linha in matriz:
        for numero_coluna in linha:
            if numero_coluna == numero:
                ocorrencias=ocorrencias+1
    return ocorrencias