def media_matriz(mat):
    """dada uma matriz de inteiros nao vazia, retorna a 
    media de todos os numeros dessa
    list(of lists)->float"""
    somap=[]
    quant=[]
    for linha in mat:
        somap.append(sum(linha))
        quant.append(len(linha))
    somaf=sum(somap)
    divid=sum(quant)
    return round(somaf/divid,2)