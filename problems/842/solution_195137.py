def ida (gol1,gol2):
    if gol1 > gol2:
        return [3,0]
    elif gol1 == gol2:
        return [1,1]
    else:
        if gol1< gol2:
            return [0,3]

def volta (gol3,gol4):
    if gol3>gol4:
        return[0,3]
    elif gol3==gol4:
        return [1,1]
    else:
        gol3<gol4:
            return [3,0]
    
    

def pontos_por_time (lista):
    time1 = lista[0]
    time2= lista[1]
    pontosidat1= time1[2][0]
    pontosvoltat1= time1[2][1]
    pontosidat2= time2[2][0]
    pontosvoltat2= time2[2][1]
    timeA= jogos(lista)[0]+ jogos(lista)[0]
    timeB= jogos(lista)[1]+ jogos(lista)[1]
    if timeA>=timeB:
        return {time1[0]:timeA,time2[0]:timeB}
    else:
        if timeB>timeA:
            return {time2[0]:timeB,time2[0]:timeA}