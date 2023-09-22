def pontos_por_time(jogo12):
    jogo1=jogo12[0]
    jogo2=jogo12[1]    
    dicionario={jogo1[0]:0,jogo2[0]:0}
    if jogo1[2][0]>jogo1[2][1]:
        dicionario[jogo1[0]]=dicionario[jogo1[0]]+3
    if jogo1[2][0]==jogo1[2][1]:
        dicionario[jogo1[0]]=dicionario[jogo1[0]]+1
        dicionario[jogo2[0]]=dicionario[jogo2[0]]+1
    if jogo1[2][0]<jogo1[2][1]:
        dicionario[jogo2[0]]=dicionario[jogo2[0]]+3
    if jogo2[2][0]>jogo2[2][1]:
        dicionario[jogo2[0]]=dicionario[jogo2[0]]+3
    if jogo2[2][0]==jogo2[2][1]:
        dicionario[jogo1[0]]=dicionario[jogo1[0]]+1
        dicionario[jogo2[0]]=dicionario[jogo2[0]]+1
    if jogo2[2][0]<jogo2[2][1]:
        dicionario[jogo1[0]]=dicionario[jogo1[0]]+3
    return dicionario