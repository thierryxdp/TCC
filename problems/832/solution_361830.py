def eh_quadrada(matriz):
    ''''''
    vazia=matriz''
    
    for linha in matriz:
        if len(linha)!=len(matriz):
            return False
        if len(linha)==len(matriz):
            return True
        if len(vazia):
            return True