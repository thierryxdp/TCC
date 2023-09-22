def melhor_volta(mat):
    """retorna uma tupla que informa de quem foi a melhor volta, o tempo e em qual volta; list->tuple"""
    melhores=[]
    for i in range(len(mat)):
        list.append(melhores,min(mat[i]))
    a=list.index(melhores,min(melhores))
    b=min(melhores)
    c=list.index(mat[a],b)+1
    return a+1,b,c