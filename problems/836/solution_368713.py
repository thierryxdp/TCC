def busca(setor,m):
    """Dada uma matriz com informações dos funcionários, retorna todos os funcionários do setor buscado, encontrados dentro da matriz.
    list,str->list"""
    l2=[]
    for i in range(len(m)):
        if setor in m[i]:
            list.remove(m[i],setor)
            l2=l2+m[i]
                        
                
    return l2