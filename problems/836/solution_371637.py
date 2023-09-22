def busca(setor,matriz):
    y=0
    for i in range(len(matriz)):
                   if setor in matriz[i]:
                		x=matriz[i].remove(2)
                		y=y+x
    return y