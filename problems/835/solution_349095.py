def melhor_volta(l):
    ''' Função que analisa uma lista l com uma matriz que contém os tempos dos corredores
    e informa quem teve o menor tempo. list-> tupla'''
    m=[]
    f=[]
    for i in range(len(l)):
        for j in range(len(l[0])):
            t=min(l[i])
            list.append(m,t)
            list.append(f,((i+1),t,j))
    g=list.index(min(m))
    return f[g]