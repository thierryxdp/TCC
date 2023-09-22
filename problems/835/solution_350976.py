def melhor_volta(tempos):
    """funcao que dada uma matriz 6x10 contendo os tempos em segundos dos corredores, retorna quem obteve a melhor volta (corredor 1 ao 6), qual foi o seu tempo e em que volta
    list(list)--->tuple"""
    lista_tempos=[]
    for i in range(len(tempos)):
        menor_tempo=min(tempos[i])
        for j in range(len(tempos[0])):
            if menor_tempo==tempos[i][j]:
                dados_menor_tempo=[i+1,menor_tempo,j+1]
                list.append(lista_tempos,dados_menor_tempo)
    return lista_tempos