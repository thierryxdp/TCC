def conta_frases(texto):
    '''Recebe uma string texto e calcula o se número de frases com 
    base nas pontuações do texto.
    Assinatura: string -> int'''
    r = len(texto.split('...'))-1
    p = len(texto.split('.')) -1 
    i = len(texto.split('?'))-1
    e = len(texto.split('!'))-1 -2
    return (r+p+i+e)