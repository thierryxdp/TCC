def conta_numero(numero,matriz):
    """recebe um número inteiro e uma matriz de inteiros de tamanhoo qualquer,conta e retorna quantas vezes aquele número aparece na matriz;int,list->int"""
    qtd=0
    for lista in matriz:
        for valor in lista:
            if valor==numero:
                qtd=qtd+1
    return qtd