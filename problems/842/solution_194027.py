def pontos_por_time(Lista):
    """calcula e retorna o estado de um time em um campeonato:List->dic"""
    empate=1
    vitora1=3
    vitoria2=3
    if Lista[0[2:[0]]]==intLista[0[2:[1:]]]:
        return empate
    elif Lista[0[2:[0]]]>=Lista[0[2:[1:]]]:
        return vitoria1
    elif Lista[0[2:[0]]]<=Lista[0[2:[1:]]]:
        return vitoria2
    elif Lista[1:[2:[0]]]==Lista[0[2:[1:]]]:
        return empate
    elif Lista[1:[2:[0]]]>=Lista[0[2:[1:]]]:
        return vitoria2
    elif Lista[1:[2:[0]]]<=Lista[0[2:[1:]]]:
        return vitoria1
    
    pontuacao= {lista[0[0]]:empate+vitoria1+empate+vitoria1,lista[0[1:]]:empate+vitoria2+empate+vitoria2}
    return pontuacao