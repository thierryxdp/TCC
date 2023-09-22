def pontos_por_time(listajogos):
    '''funcao que recebe uma lista de dois elementos no qual cada elemento tambem e uma lista que contem informacoes sobre o nome dos times e o saldo de gols nos jogos;
       lista(lista(str,str,lista(int,int)),lista(str,str,lista(int,int)))->dicionary'''
    resultado1=[]
    resultado2=[]
    if listajogos[0][2][0]>listajogos[0][2][1]:
    resultado1 =[3,0]
    if listajogos[0][2][0]==listajogos[0][2][1]:
    resultado1= [1,1]
    if listajogos[0][2][0]<listajogos[0][2][1]:
    resultado1=[0,3]     
    if listajogos[1][2][0]>listajogos[1][2][1]:
    resultado2= [3,0]
    if listajogos[1][2][0]== listajogos[1][2][1]:
    resultado2= [1,1]
    if listajogos[1][2][0]<listajogos[1][2][1]:
    resultado2= [0,3]
    resultadofinal= (resultado1[0]+resultado2[0],resultado1[1]+resultado2[1])
    placar={listajogos[0][0]:resultado[0],listajogos[0][1]:resultado[1]}

    return placar