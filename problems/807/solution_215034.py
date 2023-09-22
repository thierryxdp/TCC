def conta_frases(t):
    '''Função que tendo um texto como entrada retorna a quantidade de
    frases existentes nesse texto
    str -> int'''
    q= str.spli(t,'.','!','?','...')
    return len(q)