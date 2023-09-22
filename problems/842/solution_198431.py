def pontos_por_time(lista):
    '''calcula a pontuação de um time na fase retornando seu nome e pontuação;
    list[str, srt, list[int, int], str, str, list[int, int]]->list[str, int]'''
    def jogo(lista):
        '''calcula os resultados dos jogos;
        list->dici'''
        dici={lista[0]:0,lista[1]:0}
        if lista[2][0]>lista[2][1]:
            dici[lista[0]]=dici[lista[0]]+3
            return dici
        elif lista[2][0]==lista[2][1]:
            dici[lista[0]]=dici[lista[0]]+1
            dici[lista[1]]=dici[lista[1]]+1
            return dici
        else:
            dici[lista[1]]=dici[lista[1]]+3
            return dici
    a=jogo(lista[0])
    b=jogo(lista[1])
    b[lista[0][0]]=b[lista[0][0]]+a[lista[0][0]]
    b[lista[0][1]]=b[lista[0][1]]+a[lista[0][1]]
    return b