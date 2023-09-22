def repetidos(x):
    """
    Recebe uma lista de numeros e retorna o numero de vezes que um
    elemento da lista é igual ao anterior;
    list -> int
    """
    x = x.sort()
    y = []
    h = []
    i = 0
    
    while i < len(x)-1: 
    	if x.count(x[0]) >= 2:
        y = x.append(x[0])
        elif y[0] != y[1]:
            h = h.append(y[0])
        i=i+1
    
    return len(h)