def melhor_volta(tempos):
    """
    
    """
    melhorestempos=[]
    melhorvolta=[]
    for i in range(len(tempos)):
        listatempos=[]
        for j in range(len(tempos[i])):
            listatempos+=[tempos[i][j]]
        list.append(melhorvolta,(list.index(listatempos,min(listatempos))))
       	melhorestempos+=min(listatempos)
  	
    corredor=list.index(melhorestempos,min(melhorestempos))+1
    return (corredor,min(melhorestempos),melhorvolta[corredor-1])