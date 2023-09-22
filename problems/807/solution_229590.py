def conta_Frases(texto):
    ''' recebe um texto e diz quantas frases há contando suas limitações
    que são : frases que terminam em .,...,!,?'''
    p1 == str.count('texto', '.')
    p2 == str.count('texto', '?')
    p3 == str.count('texto', '!')
    p4 == str.count('texto', '...')
    return p1 + p2 + p3 + p4 + (p4*(-3))