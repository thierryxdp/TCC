def conta_frases(texto):
    '''
       Função que recebe uma string contendo frases, as separa de acordo com suas pontuações
       como o ponto no final da frase, exclamação, interrogação e reticençias.
       Retorna o numero de frases contidas na string inicial(texto).
       str --> int
    '''
    frases = texto
    ponto = frases.index('.')
    exclamacao = frases.index('!')
    interrogacao = frases.index('?')
    reticencias = frases.index('...')
    
    fatiamento1 = frases[0:ponto]+'.'
    fatiamento2 = frases[ponto:exclamacao]+'!'
    fatiamento3 = frases[exclamacao:interrogacao]+'?'
    fatiamento4 = frases[interrogacao:]

    correcao2 = fatiamento2.replace('.','')
    correcao3 = fatiamento3.replace('!','')
    correcao4 = fatiamento4.replace('?','')

    numero_frases = (fatiamento1,correcao2,correcao3,correcao4)

    return len(numero_frases)