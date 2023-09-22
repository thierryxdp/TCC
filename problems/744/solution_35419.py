def hashtag(s):
    tamanho_string = len(s)
    meio_string = -(-tamanho_string//2)
    
    l = list(s)
    l.insert(0, '#')
    l.insert(meio_string, '#')
    l.append('#')
    s = ''.join(l)
    return s