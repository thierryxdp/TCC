def eh_quadrada(matriz):
    """identifica se a matriz recebida é quadrada.
    list->bool"""
    contaLin=0
    contaCol=0
    for linha in matriz:
        contaCol=contaCol+1
        for valor in linha:
            contaLin=contaLin+1
    if contaLin==contaCol**2:
        return true
    else:
        false