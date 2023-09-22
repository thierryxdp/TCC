def pontos_por_time(lista):
    '''funcao que dada uma lista contendo outras listas:
       L1 e L2 informando o nome do time e o numero de 
       gols em dois jogos de futebol entre esses  dois 
       times, retorna um dicionario cujos mapeamentos 
       sao: <nome do time>-><numero total de pontos>.
       O numero total é dado por 3* numero de vitoria +
       1*o numero de empate
       lista->dicionario'''
    time1=(lista[0])[0]
    pontuacao1=((lista[0])[2])[0]
    time1=(lista[1])[1]
    pontuacao2= ((lista[1])[2])[1]
    time2=(lista[0])[1]
    pontua1=((lista[0])[2])[1]
    pontua2=((lista[1])[2])[0]
    listavazia1=[]
    listavazia2=[]
    if pontuacao1>pontua1:
            listavazia1=listavazia1+[3]
    if pontuacao2> pontua2:
            listavazia1=listavazia1+[3]
    if pontua1>pontuacao1:
            listavazia2=listavazia2+[3]
    if pontua2>pontuacao2:
            listavazia2=listavazia2+[3]
    return{time2:((listavazia2[0]) +  (listavazia2[1])), time1:((listavazia1[0]) + (listavazia1[1]))}