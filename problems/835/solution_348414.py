def melhor_volta(matriz):
    '''Funcao que retorna qual corredor fez a melhor volta.
    list->tuple'''
    x=min(matriz[0])
    y=min(matriz[1])
    z=min(matriz[2])
    k=min(matriz[3])
    j=min(matriz[4])
    i=min(matriz[5])
    a=[x,y,z,k,j,i]
    l=min(a)
    if l==x:
        return 1,list.index(matriz[0],x)+1
    if l==y:
        return 2,list.index(matriz[1],y)+1
    if l==z:
        return 3,list.index(matriz[2],z)+1
    if l==k:
        return 4,list.index(matriz[3],k)+1
    if l==j:
        return 5,list.index(matriz[4],j)+1
    if l==i:
        return 6,list.index(matriz[5],i)+1