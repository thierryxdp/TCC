def busca(n,l):
     ''' Função que analisa uma matriz e devolve as colunas que possuem a string n,
list, string -> list'''
    m=[]
    for i in range(len(l)):
        if(l[i][1]==n):
            list.append(m,l[:1]+l[2:])
    return m