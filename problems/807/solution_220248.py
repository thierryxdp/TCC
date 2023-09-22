def conta_frases(texto):
    '''funcao que dada um texto retona 
    a quantidade de frases.
    entrada: string
    saida: inteiro
    '''
    pontos= texto.split('.')
    exclamacao= texto.split('!')
    interrogacao= texto.split('?')
    reticencias= texto.split('...')
    return (len(pontos)-len(reticencias))+len(exclamacao)+len(interrogacao)