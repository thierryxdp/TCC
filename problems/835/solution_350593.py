def melhor_volta(tempos):
    """
    Função recebe uma matriz 6x10  com os tempos em segundos dos
    corredores em cada volta. Retorna uma tupla informando: de quem
    foi a melhor volta da prova, com qual tempo e em que volta.
    matriz -> tuple
    """
    melhorestempos=[]
    melhorvolta=[]
    for i in range(len(tempos)):
        listatempos=[]
        for j in range(len(tempos[i])):
            listatempos+=[tempos[i][j]]
        list.append(melhorvolta,(list.index(listatempos,min(listatempos))+1))
       	
        melhorestempos+=[min(listatempos)]
  	
    corredor=list.index(melhorestempos,min(melhorestempos))+1
    return (corredor,min(melhorestempos),melhorvolta[corredor-1])