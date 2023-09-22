def conta_frases(texto):
    '''Recebe uma string texto e calcula o se número de frases com 
    base nas pontuações do texto.
    Assinatura: string -> int'''
    frase=0
    for x in texto:
        if x=='!'or x=='?' or x=='.':
            frase = frase + 1 
    reticencias = len(texto.split('...')-1        
    return (frase+reticencias)