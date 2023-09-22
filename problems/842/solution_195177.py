def pontos_por_time(lista):
    dicionario={lista[0][0]:0,lista[0][1]:0}
    jogo_ida=lista[0][2]
    jogo_volta=lista[1][2]
    if jogo_ida[0]>jogo_ida[1]:
        dicionario[lista[0][0]]+=3
    elif jogo_ida[0]<jogo_ida[1]:
         dicionario[lista[0][1]]+=3
    else:
        dicionario[lista[0][0]]+1
        dicionario[lista[0][1]]+1
    if  jogo_volta[0]>jogo_volta[1]:
        dicionario[lista[0][1]]+=3
    elif jogo_ida[0]<jogo_ida[1]:
         dicionario[lista[0][0]]+=3
    else:
        dicionario[lista[0][0]]+1
        dicionario[lista[0][1]]+1
        return dicionario