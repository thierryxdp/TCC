def melhor_volta1(matriz):
    """ """
    melhores=(0,0,0)
    lista=[]
    for i in range(6):
        for j in range(10):
            if matriz[i][j]< matriz[i][j-1]:
                lista=lista+ [matriz[i][j]]
    melhores=(i+1,min(lista),j+1)        
    return melhores