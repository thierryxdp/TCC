def conta_frases(s):
    '''dado um texto armazenado em uma string(s), retorna o número de frases que aparecem no texto;
    str -> int'''
    s1 = s.replace('...','.')
    n = s1.count('.') + s1.count('!') + s1.count('?')
    if n == 1 and (s1[-1] == '.' or '!' or '?' or '...'):
        return 1
    elif n == 1:
        return 2
    else:
        return n