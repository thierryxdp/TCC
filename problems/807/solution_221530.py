def conta_frases(y):
    '''A função separa a frase por ponto final, ponto de exclamação, ponto de interrogação
    ou três pontos em sequência (reticências) e retorna, com base nesse critério,
    quantas frases será formada
    str->int'''
    
    b = 0
    a = 0
    i = 0
    x = ['.','!','?','...']
    
    while len(y)>i:
        if x[a] == y[i] and y[i+1] != x[a]:
            z = str.split(str.count(y,x[i]))
            a = a + 1
            b = b + z
        i = i + 1
        
    return b
        
    return a