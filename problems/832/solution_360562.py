def eh_quadrada(matriz):
    """identifica se a matriz recebida é quadrada.
    list->bool"""
    contalin=0
    contacol=0
    for linha in matriz:
        contalin=contalin+1
        for valor in linha:
            contacol=contacol+1
    if contalin==contacol/contalin or matriz=[]:
        return True
    else:
        return False