def pontos_por_time(lista): 
    '''
       Dado uma lista contendo duas lista em que a primeira
       é referente ao jogo 1 da fase e a segunda referente 
       ao jogo 2 da fase e retorna a quantidade de pontos 
       que cada time fez na fase após os dois jogos
       list -> dict
    '''
    lista1 = lista[0]
    lista2 = lista[1]
    jogo1 = lista1[2]
    jogo2 = lista2[2]
    if str(lista1[0]) == str(lista2[0]):
        if jogo1[0] > jogo1[1] and jogo2[0] > jogo2[1]:
            return {lista1[0]:6, lista1[1]:0}
        elif jogo1[0] > jogo1[1] and jogo2[0] < jogo2[1]:
            return {lista1[0]:3, lista1[1]:3}
        elif jogo1[0] < jogo1[1] and jogo2[0] < jogo2[1]:
            return {lista1[0]:0, lista1[1]:6}
        elif jogo1[0] == jogo1[1] and jogo2[0] == jogo2[1]:
            return {lista1[0]:2, lista1[1]:2}
        elif jogo1[0] > jogo1[1] and jogo2[0] == jogo2[1]:
            return {lista1[0]:4, lista1[1]:1}
        elif jogo1[0] == jogo1[1] and jogo2[0] > jogo2[1]:
            return {lista1[0]:4, lista1[1]:1}
        elif jogo1[0] == jogo1[1] and jogo2[0] < jogo2[1]:
            return {lista1[0]:1, lista1[1]:4}
        elif jogo1[0] < jogo1[1] and jogo2[0] > jogo2[1]:
            return {lista1[0]:3, lista1[1]:3}
        elif jogo1[0] < jogo1[1] and jogo2[0] == jogo2[1]:
            return {lista1[0]:1, lista1[1]:4}
    elif str(lista1[0]) != str(lista2[0]):
        if jogo1[0] > jogo1[1] and jogo2[0] > jogo2[1]:
            return {lista1[0]:3, lista[1]:3}
        elif jogo1[0] > jogo1[1] and jogo2[0] < jogo2[1]:
            return {lista1[0]:6, lista1[1]:0}
        elif jogo1[0] < jogo1[1] and jogo2[0] < jogo2[1]:
            return {lista1[0]:3, lista1[1]:3}
        elif jogo1[0] == jogo1[1] and jogo2[0] == jogo2[1]:
            return {lista1[0]:2, lista1[1]:2}
        elif jogo1[0] > jogo1[1] and jogo2[0] == jogo2[1]:
            return {lista1[0]:4, lista1[1]:1}
        elif jogo1[0] == jogo1[1] and jogo2[0] > jogo2[1]:
            return {lista1[0]:1, lista1[1]:4}
        elif jogo1[0] == jogo1[1] and jogo2[0] < jogo2[1]:
            return {lista1[0]:4, lista1[1]:1}
        elif jogo1[0] < jogo1[1] and jogo2[0] > jogo2[1]:
            return {lista1[0]:6, lista1[1]:0}
        elif jogo1[0] < jogo1[1] and jogo2[0] == jogo2[1]:
            return {lista1[0]:1, lista1[1]:4}