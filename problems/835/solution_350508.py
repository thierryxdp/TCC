def melhor_volta(placar):
    '''Funcao que, recebendo como entrada uma matriz em que 
    as linhas representam cada um dos 6 corredores e as 
    colunas representam os tempos das 10 voltas dadas por 
    cada corredor, retorna uma tupla que informa de quem foi a melhor 
    volta, qual foi o tempo em questao em que volta este 
    aconteceu.
    List -> Tup'''
    lin = len(placar)
    menores_tempos = []
    
    for i in range(lin):
        menores_tempos += [min(placar[i]),]
        
    menor_tempo = min(menores_tempos)
    vencedor = list.index(menores_tempos, menor_tempo) + 1
    numero_volta = list.index(placar[vencedor-1],menor_tempo) + 1
        
    return (vencedor, menor_tempo, numero_volta)