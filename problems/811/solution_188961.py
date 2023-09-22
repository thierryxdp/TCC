def colchao(medidas,H,L):
    """Função que recebe uma lista contendo as medidas ("A", "B", "C"])
    de um colchão, tal como a altura e a largura de uma porta ("H" e "L") e retorna se é possível passar o colchão pela porta.Entrada -> list,int,int; Saída -> bool"""
    
    if medidas[0] == max(medidas):
        novasmedidas = [medidas[1], medidas[2]]
        
    if medidas[1] == max(medidas):
        novasmedidas = [medidas[0], medidas[2]]
        
    if medidas[2] == max(medidas):
        novasmedidas = [medidas[0], medidas[1]]
        
    if min(novasmedidas) <= L and max(novasmedidas) <= H:
        return bool(1)
    
    if min(novasmedidas) <= H and max(novasmedidas) <= L:
        return bool(1)
    
    else:
        return bool(0)