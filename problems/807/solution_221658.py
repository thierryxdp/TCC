def conta_frases(f):
    '''
    Ele recebe um conjunto qualquer de frases. Feito isso, ele conta
    todos os possíveis pontos que fazem as separações das frases.
    Recebe e para exclamações; Recebe i para interrogações;
    Recebe r para reticências; Recebe p para pontos e subtrai das
    vezes que ocorreram reticências. Ou seja, se apareceram duas vezes,
    serão 6 pontos que não deverão ser contados. E retorna a soma.
    '''
    e = f.count('!')
    i = f.count('?')
    r = f.count('...')
    p = f.count('.')-(r*3)
    
    return e + i + r + p