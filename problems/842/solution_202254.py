def pontos_por_time(lista):
    """."""
    cor = lista[0][2]
    fla = lista[1][3]
    
    if lista[0]+[2] > lista[1][3]:
        pontos cor = 3
        pontos fla = 0
        
    if lista[0]+[2] < lista[1][3]:
        pontos cor = 0
        pontos fla = 3
        
        return {cor:pontos cor, fla:pontosfla}