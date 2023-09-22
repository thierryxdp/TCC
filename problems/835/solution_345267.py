def melhor_volta(matriz):
    lista = []
    ordem = list(range(0,6))
    ordem2 = list(range(0,9))
    t = 0
    
    for pessoa in matriz:
        a = min(pessoa)
        list.append(lista,a)
    
    b = min(lista)
    for p in ordem:
        if lista[p] == b:
            c = p + 1
    
    for pessoa in matriz:
        for tempo in pessoa:
            if tempo == b:
                lista2 = pessoa
    
    for p2 in ordem2:
        if lista2[p2] == b:
            t = p2 + 1
            
    return (c,b,t)