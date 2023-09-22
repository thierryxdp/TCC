def conta_frases(y):
    '''A função separa a frase por ponto final, ponto de exclamação, ponto de interrogação
    ou três pontos em sequência (reticências) e retorna, com base nesse critério,
    quantas frases será formada
    str->int'''
    
    a = 0
    i = 0
    x = ['.','!','?','...']
    
    while len(x)>i:
        if x[i] in y:
            a = a + 1
        i = i + 1
        
    return a