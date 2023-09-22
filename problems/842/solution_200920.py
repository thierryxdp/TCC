def pontosrodada1(lista : list) -> list:
    'Função que define os pontos da primeira rodada'
    'list -> list'
    rodada1 = []
    pontostime1a = 0
    pontostime2a = 0
    gols1 = lista[0][2][0]
    gols2 = lista[0][2][1]
    if gols1 == gols2:
        pontostime1a = pontostime1a + 1
        pontostime2a = pontostime2a + 1
        rodada1 = [pontostime1a,pontostime2a]
        return rodada1
    
    elif gols1 > gols2:
        pontostime1a = pontostime1a + 3
        rodada1 = [pontostime1a,pontostime2a]
        return rodada1
    
    elif gols1 < gols2:
        pontostime2a = pontostime2a + 3
        rodada1 = [pontostime1a,pontostime2a]
        return rodada1

def pontosrodada2(lista : list) -> list:
    'Função que define os pontos da segunda rodada'
    'list -> list'
    rodada2 = []
    gols3 = lista[1][2][0]
    gols4 = lista[1][2][1]
    pontostime1b = 0
    pontostime2b = 0
    if gols3 == gols4:
        pontostime1b = pontostime1b + 1
        pontostime2b = pontostime2b + 1
        rodada2 = [pontostime1b,pontostime2b]
        return rodada2
    
    elif gols3 > gols4:
        pontostime1b = pontostime1b + 3
        rodada2 = [pontostime1b,pontostime2b]
        return rodada2
    
    elif gols3 < gols4:
        pontostime2b = pontostime2b + 3
        rodada2 = [pontostime1b,pontostime2b]
        return rodada2

def pontos_por_time(lista: list) -> dict:
    'Função que define pontuação de dois times em dois jogos, dados os times e os resultados dos jogos.'
    'list -> dict'
    rodada1 = pontosrodada1(lista)
    rodada2 = pontosrodada2(lista)
    pontosfinais = [rodada1[0] + rodada2[1], rodada2[0] + rodada1[1]]
    resultados = {lista[0][0]:pontosfinais[0],
                  lista[0][1]:pontosfinais[1],
                  }
    return resultados