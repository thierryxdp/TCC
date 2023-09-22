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
    c=[f,g,h,i,a,b]
    d=min(c)
    if d==f:
        return 1,d,list.index(mat[0]),f)+1
    if d==g:
        return 2,d,list.index(mat[1]),g)+1
    if d==h:
        return 3,d,list.index(mat[2]),h)+1
    if d==i:
        return 4,d,list.index(mat[3]),i)+1
    if d==a:
        return 5,d,list.index(mat[4]),a)+1
    if d==b:
        return 6,d,list.index(mat[5]),b)+1