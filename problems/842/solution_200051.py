def pontos_por_time(x):
    '''Função que retorna um dicionário com a chave sendo um time e o valor sendo os pontos desse time, dado uma lista com duas listas dentro com os times, e o resultado dos jogos''' 
    if x[0][2][0]>x[0][2][1]:
        Pa=3 and Pb=0
    elif x[0][2][0]=x[0][2][1]:
    	Pa=1 and Pb=1
    else:
        Pa=0 and Pb=3 
    if x[1][2][1]>x[1][2][0]:
        Pa=Pa+3
    elif x[1][2][1]=x[1][2][0]:
        Pa=Pa+1 and Pb=Pb+1
    else:
        Pb=Pb+3  
    return {x[0][0]= Pa,x[0][1]=Pb}