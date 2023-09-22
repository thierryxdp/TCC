def conta_frases(texto):
    '''Recebe uma string texto e calcula o se número de frases com 
    base nas pontuações do texto.
    Assinatura: string -> int'''
    for x in texto:
        if x=='!'or x=='?' or x=='...':
            x='.'
    lista=texto.split('.')
    return (lista)