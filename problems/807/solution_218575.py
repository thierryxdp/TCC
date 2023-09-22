def conta_frases(frase):
    """ Função que contabaliza o número de frases de acordo 
    com a pontuação
    Entrada: String
    Saída: String """
    p = str.count(frase,'.',-1)   
    e = str.count(frase,'!',-1)
    i = str.count(frase,'?')
    p3 = str.count(frase,'...')
    
    return p+e+i+p3