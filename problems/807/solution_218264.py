def conta_frases(frase):
    """ Função que contabaliza o número de frases de acordo 
    com a pontuação
    Entrada: String
    Saída: String """
    p = str.split(frase,'.')   
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    p3 = str.split(frase,'...')
    x = len(p)-1
    y = len(e)-1
    z = len(i)-1
    k = len(p3)
    return x+y+z