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
    pontuatotal= int(str(lista[0])[2])[1]+ int(str(lista[1])[2])[0]
    pontuacaototal= int(str(lista[0])[2])[0] + int(str(lista[1])[2])[1]
    
 
        
    pontuatotal= pontua1 + pontua2
    pontuacaototal= pontuacao2+ pontuacao1
     
         
    return{time2:pontuatotal, time1:pontuacaototal}#Start your python function here