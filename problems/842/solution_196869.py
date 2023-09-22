def pontos_por_time(lista):
    lista1=lista[0]#referente ao 1 jogo
    lista2=lista[1]#referente ao 2 jogo
    lista3=lista1[0],lista1[1]#referente aos times do 1 jogo
    lista4=lista1[2]#referente a pontuacao dos times do 1 jogo
    lista5=lista2[0],lista2[1]#referente aos times do 2 jogo
    lista6=lista2[2]#referente a pontuacao dos times do 2 jogo
    #lista1[0]=lista2[1] primeiro time
    #lista1[1]=lista2[0] segundo time
    if  lista4[0]==lista4[1] and  lista6[0]==lista6[1]:#empate
        return{lista1[0]:lista4[0]+lista6[1],lista1[1]:lista4[1]+lista6[0]}
    elif lista4[0]>list4[1] and lista6[0]<lista6[0]:#1v1v
		return{lista1[0]:(lista4[0]+lista6[1])*3,lista1[1]:0} 
    elif lista4[0]<list4[1] and lista6[0]>lista6[0]:#2v2v
        return{lista1[0]:0,lista1[1]:(lista4[1]+lista6[0])*3}
    elif lista4[0]>list4[1] and lista6[0]>lista6[0]:#1v2v
        return {lista1[0]:(lista4[0]+lista6[1])*3,lista1[1]:(lista4[1]+lista6[0])*3}
    else:#2v1v
        return {lista1[0]:(lista4[0]+lista6[1])*3,lista1[1]:(lista4[1]+lista6[0])*3}