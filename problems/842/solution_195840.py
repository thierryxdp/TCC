''' list(list,list) -- > dict'''

def pontos_por_time(lista):
    jogo1_times = {'Casa': lista[0][0], 'Fora': lista[0][1]}
    jogo2_times = {'Casa': lista[1][0], 'Fora': lista[1][1]}
    jogo1_placar = {'Casa': lista[0][2][0], 'Fora': lista[0][2][1]} 
    jogo2_placar = {'Casa': lista[1][2][0], 'Fora': lista[1][2][1]}

    if jogo1_placar['Casa'] >= jogo1_placar['Fora']:
        if jogo1_placar['Casa'] == jogo1_placar['Fora']:
            Pontos_jogo1 = {'Casa':1,'Fora':1}
        else:
            Pontos_jogo1 = {'Casa':3,'Fora':1}
    if jogo1_placar['Casa'] < jogo1_placar['Fora']:
        Pontos_jogo1 = {'Casa':1,'Fora':3}

        
    if jogo2_placar['Casa'] >= jogo2_placar['Fora']:
        if jogo2_placar['Casa'] == jogo2_placar['Fora']:
            Pontos_jogo2 = {'Casa':1,'Fora':1}
        else:
            Pontos_jogo2 = {'Casa':3,'Fora':1}
    if jogo2_placar['Casa'] < jogo2_placar['Fora']:
        Pontos_jogo2 = {'Casa':1,'Fora':3}

    i = 'Casa'
    j = 'Fora'
    pontuacao = {jogo1_times[i]: Pontos_jogo1[i] + Pontos_jogo2[j], jogo1_times[j]: Pontos_jogo1[j] + Pontos_jogo2[i]}
    return pontuacao