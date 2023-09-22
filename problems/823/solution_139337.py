def faltant(x):
    '''funcao que retorn qual numero na sequencia esta faltando. list->int'''
    i=0
    s=[]
    list.sort(x)
    while i<len(x)+1:
        s=s+[i+1,]
        i=i+1
    y= sum(s)
    z= sum(x)
    return y-z