def repedidos(listas):
    repeticao = 0
    i = 0
    while i<len(listas)-1:
        if listas[i]==listas[i+1]:
            repeticao=repeticao+1
        i = i+1
    return repeticao