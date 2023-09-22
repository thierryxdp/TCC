def melhor_volta(l):
    ''' Função que analisa uma lista l com uma matriz que contém os tempos dos corredores
    e informa quem teve o menor tempo. list-> tupla'''
    m=[]
    f=[]
    for i in range(len(l)):
        t=min(l[i])
        g=list.index(l[i],t)
        list.append(m,t)
        list.append(f,(i+1,t,g+1))
    c=min(m)
    return f[list.index(m,c)]