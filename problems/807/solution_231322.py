def conta_frases(texto):
    '''Recebe uma string texto e calcula se número de frases com 
    base nas pontuações do texto.
    Assinatura: string -> int'''
    r = len(texto.split('...'))-1
    p = len(texto.split('.')) -1 -3
    i = len(texto.split('?'))-1
    e = len(texto.split('!'))-1
    return (r+p+i+e)