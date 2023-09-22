def conta_frases(texto):
    '''
       Dado um texto a função retorna quantas frases estão
       presentes nesse texto baseado nos pontos de conclusão
       no final de cada frase
       str -> int
    '''
    return len(str.split('.')) + len(str.split('!')) + len(str.split('?')) + len(str.split ('...'))