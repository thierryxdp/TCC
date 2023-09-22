def pontos_por_time (lista):
    '''função que retorna um dicionario com os pontos de cada time; 
    list->dicionario'''
    jogo1= lista[:len(lista)/2]
    jogo2= lista[len(lista)/2:]
    if jogo1[2][0]>jogo1[2][1]:
        jogo1[0]=3
    if jogo1[2][0]<jogo1[2][1]:
        jogo1[1]=3
    if jogo2[2][0]>jogo2[2][1]:
        jogo2[0]=3
    if jogo2[2][0]<jogo2[2][1]:
        jogo2[1]=3
    if jogo1[2][0]==jogo1[2][1]:
        jogo1[0]==1
    if jogo1[2][0]==jogo1[2][1]:
        jogo1[1]==1
    if jogo2[2][0]==jogo2[2][1]:
        jogo2[0]==1
    if jogo2[2][0]==jogo2[2][1]:
        jogo2[1]==1
    return {lista[0]:}