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
    
    fatiamento1 = frases[0:ponto]+'.' or frases[0:exclamacao]+'!' or frases[0:interrogacao]+'?' or frases[0:reticencias]+'...'
    fatiamento2 = frases[ponto:exclamacao]+'!' or frases[ponto:interrogacao]+'?' or frases[ponto:reticencias]+'...' or frases[ponto:ponto]+'.'
    fatiamento3 = frases[exclamacao:interrogacao]+'?' or frases[exclamacao:ponto]+'.' or frases[exclamacao:reticencias]+'...' or frases[exclamacao:exclamacao]+'!'
    fatiamento4 = frases[interrogacao:reticencias]+'...' or frases[interrogacao:ponto]+'.' or frases[interrogacao:exclamacao]+'!' or frases[interrogacao:interrogacao]+'?'

    correcao2 = fatiamento2.replace('.','')
    correcao3 = fatiamento3.replace('!','')
    correcao4 = fatiamento4.replace('?','')

    numero_frases = (fatiamento1,fatiamento2,fatiamento3,fatiamento4)

    return len(numero_frases)