pontos_por_time(nome1 = " ",nome2 = " ", pontos1,pontos2):
    '''funcao que retorna o nome do time e numero de pontos'''
    lista = [nome1,nome2[pontos1,pontos2]]
    if (pontos1>pontos2):
        return lista[nome1 + [pontos1 + 3] + nome2 + pontos2]
    elif (pontos2>pontos1):
        return lista[nome2 + [pontos2 + 3] + nome1 + pontos1]
    elif (pontos1==pontos2):
        return lista[nome1 + [pontos1 + 1] + nome2 + pontos2 + 1]