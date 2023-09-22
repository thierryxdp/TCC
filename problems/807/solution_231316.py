def conta_frases(texto):
    '''Recebe uma string texto e calcula o se número de frases com 
    base nas pontuações do texto.
    Assinatura: string -> int'''
    frase=0
    for x in texto:
        if x=='!'or x=='?':
            frase = frase + 1 
    r = len(texto.split('...'))-1
    p = len(texto.split('.')) -1 
    i = len(texto.split('?'))-1
    e = len(texto.split('!'))-1
    return (r+p+i+e)