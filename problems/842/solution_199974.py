def pontos_por_time(lista):
    """retorna duas listas contendo as informações a respeito de dois jogos entre
    dois times(jogo 1 e jogo 2)
    list[list,list] -> dict"""
#[['time1','time2',[pontuacao1,pontuacao2]], ['time2','time1', [pontuacao2, pontuacao1]]]
 
if jogo1[2][0] > jogo1[2][1]:
        dicionario[jogo1[0]] = dicionario[jogo1[0]] + 3
        
    if jogo1[2][0] == jogo1[2][1]:
        dicionario[jogo1[0]] = dicionario[jogo1[0]] + 1
        dicionario[jogo1[1]] = dicionario[jogo1[1]] + 1
        
    if jogo1[2][0] < jogo1[2][1]:
        dicionario[jogo1[1]] += 3

    if jogo2[2][0] > jogo2[2][1]:
        dicionario[jogo1[1]] = dicionario[jogo1[1]] + 3 
        
    if jogo2[2][0] == jogo2[2][1]:
        dicionario[jogo1[0]] = dicionario[jogo1[0]] + 1
        dicionario[jogo1[1]] = dicionario[jogo1[1]] + 1
        
    if jogo2[2][0] < jogo2[2][1]:
        dicionario[jogo1[0]] += 3

    return dicionario