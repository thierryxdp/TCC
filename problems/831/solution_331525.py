def lingua_p(palavra):
    '''função que dada uma palavra, retorna essa palavra
    com todas as suas vogais seguidas da letra p str -> str'''
    
    p = 'p'
    palavrap = ''
    for vogalp in palavra:
        if vogalp in 'aeiouAEIOU':
            vogalp = vogalp + p + vogalp
        palavrap = palavrap + vogalp
    str.lower(palavrap)
    return palavrap