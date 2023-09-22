def busca(s,m):
    '''funçao que recebe uma matriz; 
    str->list'''
    r=[]
    for linha in range(len(m)):
        if s==m[linha][2]:
            list.remove(m[linha],s)
            list.append(r,m[linha])
    return r