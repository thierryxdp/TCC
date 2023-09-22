def pontos_por_time(lEntrada):
    '''Retorna um dicionário com os números de pontos de cada
       time, acessados pelos seus respectivos nomes e calculados
       a partir da lista de entrada;
       list -> dictionary'''
    golsIdaCor=lEntrada[0][2][0]
    golsIdaFla=lEntrada[0][2][1]
    
    golsVoltaCor=lEntrada[1][2][1]
    golsVoltaFla=lEntrada[1][2][0]
    
    ptsCor=0
    ptsFla=0
    
    if golsIdaCor>golsIdaFla:
        ptsCor+=3
    elif golsIdaCor<golsIdaFla:
        ptsFla+=3
    else:
        ptsCor+=1
        ptsFla+=1
    
    if golsVoltaCor>golsVoltaFla:
        ptsCor+=3
    elif golsIdaCor<golsVoltaFla:
        ptsFla+=3
    else:
        ptsCor+=1
        ptsFla+=1
    
    return {'Cormengo':ptsCor,'Flamínthians':ptsFla}