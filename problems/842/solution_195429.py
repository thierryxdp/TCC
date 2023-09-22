def pontos_por_time(listajogos):
    '''funcao que recebe uma lista de dois elementos no qual cada elemento tambem e uma lista que contem informacoes sobre o nome dos times e o saldo de gols nos jogos;
       lista(lista(str,str,lista(int,int)),lista(str,str,lista(int,int)))->dicionary'''
    resultado1=[]
    resultado2=[]
    pontosida1= listajogos[0][2][0]
    pontosida2= listajogos[0][2][1]
    pontosvolta1= listajogos[1][2][0]
    pontosvolta2= listajogos[1][2][1]
    if pontosida1>pontosida2:
        resultado1= [3,0]
    if pontosida1==pontosida2:
        resultado1= [1,1]
    if pontosida1<pontosida2:
        resultado1=[0,3]
    if pontosvolta1>pontosvolta2:
        resultado2= [3,0]
    if pontosvolta1==pontosvolta2:
        resultado2= [1,1]
    if pontosvolta1<pontosvolta2:
        resultado2=[0,3]
    pontostotal= (resultado1[0]+resultado2[1],resultado1[1]+resultado2[0])
    placarfinal={listajogos[0][0]:pontostotal[0],listajogos[0][1]:pontostotal[1]}
    return placarfinal