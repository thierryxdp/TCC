def pontos_por_time(l1):
    '''Função que dado informações do número de gols em dois jogos de futebol entre dois times retorna o nome do time e o número total de pontos; list-> dic''' 
    pontos1=[0,0]
    pontos2=[0,0]
    #lista1- jogo da ida

    if l1[0][2][0]>l1[0][2][1]:
        pontos1[0]=3


    if l1[0][2][0]<l1[0][2][1]:
        pontos2[0]=3


    if l1[0][2][0]==l1[0][2][1]:
        pontos1[0]=1
        pontos2[0]=1
        
    #lista2- jogo da volta
    if l1[1][2][0]>l1[1][2][1]:
        pontos2[1]=3

    if l1[1][2][0]<l1[1][2][1]:
        pontos1[1]=3
    
    if l1[1][2][0]==l1[1][2][1]:
        pontos1[1]=1
        pontos2[1]=1

    dic={l1[0][0]:pontos1[0]+pontos1[1], l1[0][1]:pontos2[0]+pontos2[1]}
    return dic