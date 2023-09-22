def melhor_volta(tempos):
    """dados os tempos de cada volta dos corredores, retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta;
    list(list) -> tuple"""
    tempos2=[]
    
    for i in tempos:
        for j in i:
        	list.append(tempos2,j)
            
    for a in tempos:
        for b in a:
            if b==min(tempos2):
                x=list.index(tempos,a)
                y=list.index(a,b)
            
    m=tuple(x+1,min(tempos2),y+1)           
    
    return m