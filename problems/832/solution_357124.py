def eh_quadrada(matriz):
    if [] in matriz:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])-1
    if linhas == colunas:
        
        return True
    else: 
        return False