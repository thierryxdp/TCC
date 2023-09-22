def lingua_p(palavra):
    t_p = []
    c = 0 
    for letra in list(palavra):
        if letra in 'aeiouúóéíá':
            t_p.append(letra + 'p' + letra)
        else:
            t_p.append(letra)
    return ''.join(t_p)