def eh_quadrada(matriz):
    ''''''
    vazia=0
    
    for linha in matriz:
        vazia=vazia+len(linha)
    if len(linha)<0:
    return True