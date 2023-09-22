def melhor_volta(mat):
    '''funcao que retorna uma tupla informando de quem foi
    a melhor volta da prova, com qual tempo e em que volta
    list->tuple'''
    f=min(mat[0])
    g=min(mat[1])
    h=min(mat[2])
    i=min(mat[3])
    a=min(mat[4])
    b=min(mat[5])
    x=[f,g,h,i,a,b]
    y=min(x)
    if y==f:
        return 1,y,list.index(mat[0],f)+1
    elif y==g:
        return 2,y,list.index(mat[1],g)+1
    elif y==h:
        return 3,y,list.index(mat[2],h)+1
    elif y==i:
        return 4,y,list.index(mat[3],i)+1
    elif y==a:
        return 5,y,list.index(mat[4],a)+1
    elif y==b:
        return 6,y,list.index(mat[5],b)+1