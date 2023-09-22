def eh_quadrada(matriz:list)-> bool:
    """Função que, dada uma matriz,
    retorna true, caso seja quadrada, ou false,
    senão for quadrada."""
   
    quadrada = True
    
    if matriz == []:
        quadrada
        
    else:
        linhas = len(matriz)
        colunas = len(matriz[0])
        
        if linhas == colunas:
            quadrada
        else:
            quadrada = False
    
    return quadrada