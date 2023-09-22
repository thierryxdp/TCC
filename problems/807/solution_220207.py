def conta_frases(texto):
    '''funcao que dada um texto retona 
    a quantidade de frases.
    entrada: string
    saida: inteiro
    '''
    pontos= texto.split('.',0)
    exclamacao= texto.split('!',0)
    interrogacao= texto.split('?',0)
    return len(pontos)+len(exclamacao)+len(interrogacao)