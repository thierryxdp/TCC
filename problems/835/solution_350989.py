def melhor_volta(matriz):
    '''Recebe uma matriz com as 10 corridas de 6 corredores e retorna
    uma tupla informando quem teve a melhor volta, com qual tempo ele
    a completou e qual das voltas foi a melhor
    mat->tuple'''
    melhores=[]
    for corredor in matriz:
        menor=min(corredor)
        melhores=list.extend(melhores,menor)
   	return melhores