def conta_frases(frase):
    """ Função que contabaliza o número de frases de acordo 
    com a pontuação
    Entrada: String
    Saída: String """
    p = str.count(frase,'.')   
    e = str.count(frase,'!')
    i = str.count(frase,'?') or p3 = str.count(frase,'...')
    
    return p+e+i+p3