def busca(x,y):
    '''funçao que recebe uma matriz e busca por setor;
    str->list'''
    r=[]
    for linha in range(len(y)):
        if x==y[linha][2]:
            list.remove(y[linha],x)
            list.append(r,y[linha])
    return r