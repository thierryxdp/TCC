def qts_frases(string):
    '''recebe frases do usuario e retorna quantas frases foram digitadas
    sendo separadas pelos pontos final, reticencias, exclamacao e interrogacao.'''
    #pontos = '.', '...', '!', '?'
    s1 = string.replace('.', '.')
    s2 = s1.replace('...', '.')
    s3 = s2.replace('!', '.')
    s4 = s3.replace('?', '.')
    print(s4)
    frases = s4.split('.')
    print(frases)
    return print(len(frases)-1)