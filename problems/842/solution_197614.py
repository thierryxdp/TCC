def pontos_por_time(lista):
    #Cormengo primeiro flaminthiians depois
    d={}
    d['Cormengo']='6'
    d['Flaminthians']='0'
    d2={'Cormengo':'3','Flaminthians':'3'}
    d3={'Cormengo':'0','Flaminthians':'6'}
    d4={'Cormengo':'4','Flaminthians':'1'}
    d5={'Cormengo':'2','Flaminthians':'2'}
    d6={'Cormengo':'1','Flaminthians':'4'}
    if lista[2][0]>lista[2][1] and lista[5][0]>lista[5][1]:
        return d
    
    elif lista[2][0]>lista[2][1] and lista[5][0]<lista[5][1]:
        return d2
    
    elif lista[2][0]<lista[2][1] and lista[5][0]<lista[5][1]:
        return d3

    elif lista[2][0]>lista[2][1] and lista[5][0]==lista[5][1]:
        return d4
    
    elif lista[2][0]==lista[2][1] and lista[5][0]<lista[5][1]:
        return d4

    elif lista[2][0]==lista[2][1] and lista[5][0]==lista[5][1]:
        return d5

    elif lista[2][0]==lista[2][1] and lista[5][0]>lista[5][1]:
        return d6