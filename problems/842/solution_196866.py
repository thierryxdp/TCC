def pontos_por_time(lEntrada):
    '''Retorna um dicionário com os números de pontos de cada
       time, acessados pelos seus respectivos nomes e calculados
       a partir da lista de entrada;
       list -> dictionary'''
    nomeT1=lEntrada[0][0]
    nomeT2=lEntrada[0][1]
    
    golsIdaT1=lEntrada[0][2][0]
    golsIdaT2=lEntrada[0][2][1]
    
    golsVoltaT1=lEntrada[1][2][1]
    golsVoltaT2=lEntrada[1][2][0]
    
    ptsT1=0
    ptsT2=0
    
    if golsIdaT1>golsIdaT2:
        ptsT1+=3
    elif golsIdaT1<golsIdaT2:
        ptsT2+=3
    else:
        ptsT1+=1
        ptsT2+=1
    
    if golsVoltaT1>golsVoltaT2:
        ptsT1+=3
    elif golsVoltaT1<golsVoltaT2:
        ptsT2+=3
    else:
        ptsT1+=1
        ptsT2+=1
    
    return {nomeT1:ptsT1,nomeT2:ptsT2}