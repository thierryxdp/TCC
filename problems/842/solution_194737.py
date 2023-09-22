def pontos_por_time(Lista):
    """calcula e retorna o estado de um time em um campeonato:List->dic"""
    empate=1
    vitoria1=3
    vitoria2=3
    if Lista[0:1][2:][0:1]==Lista[0:1][2:][1:]:
        empate
    elif Lista[0:1][2:][0:1]>=Lista[0:1][2:][1:]:
        vitoria1
    elif Lista[0:1][2:][0:1]<=Lista[0:1][2:][1:]:
        vitoria2
    elif Lista[1:][2:][0:1]==Lista[0:1][2:][1:]:
        empate
    elif Lista[1:][2:][0:1]>=Lista[0:1][2:][1:]:
        vitoria2
    elif Lista[1:][2:][0:1]<=Lista[0:1][2:][1:]:
        vitoria1
    
    pontuacao={Lista[0][0]:empate+vitoria1+empate+vitoria1,Lista[0][1:]:empate+vitoria2+empate+vitoria2}
    
    return Lista[0][0],Lista[0][1:]