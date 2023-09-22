def conta_numero(numero,matriz):
    '''Esta função conta a ocorrencia de um numero dado em uma matriz dada.
int,list->int'''
    ocorrencia=0
    for linha in matriz:
        for aij in linha:
            if aij==numero:
                ocorrencia=ocorrencia+1
    return ocorrencia