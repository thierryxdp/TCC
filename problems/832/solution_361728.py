def eh_quadrada(matriz):
    ''''''
    vazia=0
    
    for linha in matriz:
        if len(linha)>0:
        vazia=vazia+len(linha)
    return vazia