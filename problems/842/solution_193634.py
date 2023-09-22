def pontos_por_time(lista):
    '''calcula a pontuação de um time na fase retornando seu nome e pontuação;
    list[str, srt, list[int, int], str, str, list[int, int]]->list[str, int]'''
    
    def resultado_jogo1(lista):
        '''retorna o resultado do jogo de volta;
        list[str, srt, list[int, int], str, str, list[int, int]]->list[str, int]'''
        if lista[0][2][0]>lista[0][2][1]:
            return 'vitoria '+ lista[0][0]
        elif lista[0][2][0]==lista[0][2][1]:
            return 'empate'
        else:
            return'vitoria '+ lista[0][1]

    def resultado_jogo2(lista):
        '''retorna o resultado do jogo de volta;
        list[str, srt, list[int, int], str, str, list[int, int]]->list[str, int]'''
        if lista[1][2][0]>lista[1][2][1]:
            return 'vitoria '+ lista[1][0]
        elif lista[1][2][0]==lista[1][2][1]:
            return 'empate'
        else:
            return 'vitoria '+ lista[1][1]

    resultados={lista[0][0]:0,lista[0][1]:0}

    if resultado_jogo1(lista)=='vitoria '+ lista[0][1] and resultado_jogo2(lista)=='vitoria '+ lista[1][0]:
        resultados[lista[0][1]]=6
        return resultados
    elif resultado_jogo1(lista)=='vitoria '+ lista[0][1] and resultado_jogo2(lista)== 'empate':
        resultados[lista[0][1]]=4
        resultados[lista[0][0]]=1
        return resultados
    elif resultado_jogo1(lista)=='empate' and resultado_jogo2(lista)== 'empate':
        resultados[lista[0][0]]=2
        resultados[lista[0][1]]=2
        return resultados
    elif resultado_jogo1(lista)=='vitoria '+ lista[0][0] and resultado_jogo2(lista)=='vitoria '+ lista[1][1]:
        resultados[lista[0][0]]=6
        return resultados
    elif resultado_jogo1(lista)=='vitoria '+ lista[0][1] and resultado_jogo2(lista)=='vitoria '+ lista[1][1] or resultado_jogo1(lista)=='vitoria '+ lista[0][0] and resultado_jogo2(lista)=='vitoria '+ lista[1][0]:
        resultados[lista[0][0]]=3
        resultados[lista[0][1]]=3
        return resultados
    else:
        resultados[lista[0][0]]=4
        resultados[lista[0][1]]=1
        return resultados#Start your python function here