def posLetra(string, letra, n):
    pos = -1
    qtd = 0
    
    for i in range(len(string)):
        if(string[i] == letra):
            q = q + 1
            if(q == n):
                pos =1
                break
    return pos