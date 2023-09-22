def conta_frases(texto):
    '''
    dado um texto, retorna a quantidade de frases
    presentes. Uma frase será definida como sendo
    qualquer segmento de texto terminado em
    PONTO FINAL, PONTO DE EXCLAMAÇÃO, PONTO DE
    INTERROGAÇÃO ou RETICÊNCIAS
    
    Pontos de exclamação e interrogação não devem
    ser usados em sequência
    
    string -> int
    '''
    
    retc = texto.count('...')
    ponto = texto.count('.') - retc
    inter = texto.count('?')
    excl = texto.count('!')
    quant = retc + ponto + inter + excl
    return quant