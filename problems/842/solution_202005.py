def resultado1(placar1):
    if placar1[0]>placar1[1]:
        return [3, 0]
    elif placar1[0]==placar1[1]:
    	return [1,1]
    else:
        return [0, 3]
def resultado2(placar2):
    if placar2[0]>placar2[1]:
        return [0, 3]
    elif placar2[0]==placar2[1]:
    	return [1, 1]
    else:
        return [3, 0]
def rodada(x, y):
    return x + y

def pontos_por_time(lst):
    """Recebe uma lista com sublistas e retorna um dicionário que traduz o nome do time em sua
    pontuação tabelada da rodada segundo o campeonato brasileiro de futebol
    assinatura: lista --> dicionario
    """   
    return {lst[0][1] : rodada(resultado1(lst[0][2])[1], resultado2(lst[1][2])[1])        
            ,
            lst[0][0] : rodada(resultado1(lst[0][2])[1], resultado2(lst[1][2])[1])
           }              }