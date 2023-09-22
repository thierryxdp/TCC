def conta_frases(texto):
    ''' Essa função ganha um texto e diz quantas frases a no mesmo
    ,tendo em mente que cada frase é marcada com o termino de .!?...'''
    texto == t
    p1 == str.count('t', '.')
    p2 == str.count('t', '...')
    p3 == str.count('t', '!')
    p4 == str.count('t', '?')
    p == p1,p2,p3,p4 
    if p =! 0:
        return p1+p2+p3+p4
    elif 0 == p1:
        return p3+p2+p4
    elif 0 == p2:
        return p1+p3+p4
    elif 0 == p3:
        return p1+p2+p4
    elif 0 == p4:
        return p1+p2+p3
    else 0 in p:
        return 'error'