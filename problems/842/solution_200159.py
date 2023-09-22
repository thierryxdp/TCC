def pontos_por_time(lista):
    '''Retorna um Dicionário com dois times de futebol e seus resultados, dado uma lista com nome dos dois times e seus resultados em dois jogos;
    lista =>lista'''
    jogo1 = lista[0]
    jogo2 = lista[1]
    nome1 = jogo1[0]
    nome2 = jogo1[1]
    nome3 = jogo2[0]
    nome4 = jogo2[1]
    pontos1 = jogo1[2]
    pontos2 = jogo2[2]
    x1 = pontos1[0]
    x2 = pontos1[1]
    y1 = pontos2[0]
    y2 = pontos2[1]
 
    if x1 > x2:
       a = (3,0)
    if x1 < x2:
       a = (0,3)
    elif x1 == x2:
       a = (1,1)

    elif y1 > y2:
       b = (3,0)
       
    elif y1 < y2:
       b = (0,3)
    else:
       b = (1,1)


    a1 = a[0] 
    a2 = a[1]  
    b1 = b[0] 
    b2 = b[1] 

    
   
 return({nome1:a1+b1, nome2:a2+b2})