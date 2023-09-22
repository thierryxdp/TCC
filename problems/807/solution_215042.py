def conta_frases(t):
    '''Função que tendo um texto como entrada retorna a quantidade de
    frases existentes nesse texto
    str -> int'''
    a= str.split(t,'.')
    b= str.split(t,'!')
    c= str.split(t,'?')
    d= str.split(t,'...')
    return len(a) + len(b) + len(c) + len(d)