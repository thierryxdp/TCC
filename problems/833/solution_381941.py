def conta_numero(numero,matriz):
    """Função que, dado um número inteiro e uma matriz de inteiros qualquer,
    conta e retorna quantas vezes aquele número aparece na matriz."""
    """int, list-->int"""
    ocorrencias_num=0
    ind=0
    for i in matriz:
        for j in matriz[ind]:
            if j==numero:
                ocorrencias_num+=1
        ind+=1
    return ocorrencias_num