def pontos_por_time(lista):
    '''Dado o parâmetro lista, com duas listas como seus
    elementos, tendo a quantidade de número de gols em dois
    jogos de futebol entra dois times. Função deve retornar
    um dicionário com essas informações, dando o  os nomes 
    dos times e suas pontuações;
    list -> dict'''
    
     if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
     #Quando o primeiro time ganha nos dois jogos seguidos
     #Time 1 fica com 6 pontos (por ter ganhado dois jogos 2x3 = 6)
     #Time 2 fica com zero pontos   
         dicionario={lista[0][0]:6,lista[1][0]:0}
         return dicionario
    
     elif lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
     #Quando no primeiro jogo o time 1 ganha, e no segundo o time 2 ganha
     #Time 1 fica com 3 pontos e time 2 com 3 pontos também
        dicionario={lista[0][0]:3,lista[1][0]:3}
         return dicionario
     
    elif lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #Quando no primeiro jogo o time 2 ganha, e no segundo o time 1 ganha
    #Time 1 fica com 3 pontos e time 2 com 3 pontos também
        dicionario={lista[0][0]:3,lista[1][0]:3}
        return dicionario
    
    elif lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #Quando nos dois jogos o time 2 ganhar
    #Time 2 fica com 6 pontos e time 1 com 0
        dicionario={lista[0][0]:0,lista[1][0]:6}
        return dicionario
    
    elif lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #Quando no primeiro jogo o time 1 ganhar e no segundo os dois times empatarem
    #Time 1 fica com 4 pontos (3 pontos de vitória no segundo jogo e 1 ponto de empate)
    #Time 2 fica só com 1 ponto (de empate)
        dicionario={lista[0][0]:4,lista[1][0]:1}
        return dicionario
    
    elif lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #Quando os dois times empatam no primeiro jogo e no segundo jogo o time 1 ganha
    #Time 1 fica com 4 pontos e time 2 com 1
        dicionario={lista[0][0]:4,lista[1][0]:1}
        return dicionario
    
    elif lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #Quando no primeiro jogo o time 2 ganhar e no segundo jogo os times empatarem
    #Time 2 fica com 4 pontos e time 1 com 1    
        dicionario={lista[0][0]:1,lista[1][0]:4}
        return dicionario
    
    elif lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #Quando no primeiro jogo os dois times empatarem e no segundo jogo o time 2 ganhar
    #Time 2 fica com 4 pontos e time 1 com 1
        dicionario={lista[0][0]:1,lista[1][0]:4}
        return dicionario
    
    elif lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #Quando nos dois jogos os times empatarem 
    #Time 1 fica com 2 pontos e time 2 com 2 pontos também
        dicionario={lista[0][0]:2,lista[1][0]:2}
        return dicionario