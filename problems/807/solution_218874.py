def conta_frases(texto):
    '''Função que conte o número de frases que aparecem
    neste texto
    Entrada: string
    Saída: int'''
    texto= ['.','!','?','...']
    return len(texto.split(' '))