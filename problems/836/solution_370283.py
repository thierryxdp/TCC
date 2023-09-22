def busca(n,l):
    ''' Função que analisa uma matriz e devolve as colunas que possuem a string n,
list, string -> list'''
    m=[]
    for i in range(len(l)):
        if(l[i][2]==n):
            list.remove(l[i],n)
            list.append(m,l[i})
    return m