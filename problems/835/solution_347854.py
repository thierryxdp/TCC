def melhor_volta(matriz):
    menorestempos=[]
    for i in range(len(matriz)):
        menor=min(matriz[i])
    menorestempos+=[menor]
colocado=menorestempos.index(min(menorestempos))
volta=matriz[colocado+1].index(min(menorestempos))
return(colocado+1,min(menorestempos),volta+1)