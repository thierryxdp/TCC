def conta_frases (texto):
    '''Entrada: Texto (variável do tipo string)
       
       Saída: Número de frases que aparecem no texto
       (vatiável do tipo inteiros)
       
       string -> int'''
    return texto.count('!') + texto.count('.') + texto.count('?') - 2*texto.count('...')