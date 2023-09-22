def conta_frases(texto):
    '''
       Função que recebe uma string contendo frases, as separa de acordo com suas pontuações
       como o ponto no final da frase, exclamação, interrogação e reticençias.
       Retorna o numero de frases contidas na string inicial(texto).
       str --> int
    '''
    if '...' in texto: 
       return texto.count('!')+texto.count('?')+texto.count('.')-(2*texto.count('...'))
    else:
       return texto.count('!')+texto.count('?')+texto.count('.')