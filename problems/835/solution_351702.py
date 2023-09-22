def melhor_volta(m):
    '''funcao que retorna o melhor tempo, em qual volta e qual corredor dada uma matriz 
    6x10. list-> tuple'''
    a=[]
    i=0
    for num in m:
        list.append(a,min(m[i]))
        i=i+1
    p=min(a)
    q=list.index(a,p)
    r=list.index(m[q],p)
    
    return ((q+1),p,(r+1))