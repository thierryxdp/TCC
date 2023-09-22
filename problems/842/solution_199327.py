def resultado_partida(tupla):
    ''' Retorna uma tupla com a pontuação do resultado de uma partida,
    dado uma tupla com uma sequencial com nome do time seguindo da pontuacao
    tuple -> tuple'''
    nome_a, gols_a, nome_b, gols_b = tupla

    if gols_a == gols_b:
        #Empate 1pt
        return (nome_a, 1, nome_b, 1)
    elif gols_a > gols_b:
        #Vitoria_a 3pt
        return (nome_a, 3, nome_b, 0)
    else:
        #Vitoria_b 3pt
        return (nome_a, 0, nome_b, 3)
            

def pontos_por_time(jogos):
    ''' Retorna um dicionário com a sendo a chave o nome do time e o valor a pontuação
    list -> dict '''
    p_jogo, gols_pjogo, s_jogo, gols_sjogo = (jogos[0], jogos[0][2], jogos[1], jogos[1][2])
    
    nome1, pt1, nome2, pt2 = resultado_partida((p_jogo[0], gols_pjogo[0], p_jogo[1], gols_pjogo[1]))
    nome3, pt3, nome4, pt4 = resultado_partida((s_jogo[0], gols_sjogo[0], s_jogo[1], gols_sjogo[1]))

    resultado = { nome1: pt1, nome2: pt2}
    resultado[nome3] += pt3
    resultado[nome4] += pt4
    
    return resultado