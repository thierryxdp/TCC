def conta_frases(frase):
    """ Função que contabaliza o número de frases de acordo 
    com a pontuação
    Entrada: String
    Saída: String """
    p = str.count(frase,'.',-3) 
    e = str.count(frase,'!')
    i = str.count(frase,'?') 
    p3 = str.count(frase,'...')
    conta = p
 
    return conta