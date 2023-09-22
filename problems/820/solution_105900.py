def posLetra(string, letra, n):
    k = -1
    q = 0
    
    for i in range(len(string)):
        if(string[i] == letra):
            q = q + 1
            if(q == n):
                pos =1
                break
    return k