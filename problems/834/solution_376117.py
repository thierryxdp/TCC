def media_matriz (matriz):
    """Função que, dada uma matriz de inteiros não vazia, retorna a 
    média de todos os números presentes nela."""
    """list-->float"""
    soma=0
    ind=0
    quant=0
    for i in matriz:
        for j in matriz[ind]:
            soma+=j
            quant+=1
        ind+=1
    return round(soma/quant,2)