def conta_frases(texto):
    '''Retorna o número de frases de um texto, sendo cada frase terminada por  ponto final, exclamação ou reticências;
    str = > int''
    frase1 = texto.split('.')
    frase2 = texto.split('!')
    frase3 = texto.split('?')
    frase4 = texto.count('...')
    
    return (len(frase1) - 2 * frase4) + len(frase2) + len(frase3) - 3