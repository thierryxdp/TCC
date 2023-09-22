def conta_frases(t):
    '''Função que tendo um texto como entrada retorna a quantidade de
    frases existentes nesse texto
    str -> int'''
    q= re.split(t,'.','!','?','...')
    return len(q)