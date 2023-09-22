def busca(Setor,Matriz):
    '''retorna dados dos funcionários de um setor
    str->list'''
    
    i=[]
    
    for x in range (len(Matriz)):
        if Setor==Matriz[x][2]:
            list.remove(m[x],Setor)
            list.append(i,Matriz[x])
    return i