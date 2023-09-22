def busca(l,matriz):
    
    """Função que dada uma matriz faz a busca de um setor desejado"""

    k =[]
    s=0
    
    for i in matriz:
        if l == i[2]:
            del(i[2])
            list.append(k,i)
            s = s+1
    return k