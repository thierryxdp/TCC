#Start your python function here
def pontos_por_time(lista):
    time1=lista[0][0]
    time2=lista[0][1]
    pontostime1=0
    pontostime2=0
    golstime1ida=lista[0][2][0]
    golstime1volta=lista[1][2][1]
    golstime2ida=lista[0][2][1]
    golstime2volta=lista[1][2][0]
    
    if golstime1ida==golstime2ida:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
        
    if golstime1volta==golstime2volta:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
        
    if golstime1ida>golstime2ida:
        pontostime1=pontostime1+3
    
    if golstime1ida<golstime2ida:
        pontostime2=pontostime2+3
        
    if golstime1volta>golstime2volta:
        pontostime1=pontostime1+3
        
    if golstime1volta<golstime2volta:
        pontostime2=pontostime2+3
        
    dicio={time1:pontostime1,time2:pontostime2}
    return dicio