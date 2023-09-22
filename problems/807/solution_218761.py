def conta_frases(frase):
    """ Função que contabaliza o número de frases de acordo 
    com a pontuação
    Entrada: String
    Saída: String """
    p = str.count(frase,'.',-6) 
    e = str.count(frase,'!')
    i = str.count(frase,'?') 
    p3 = str.count(frase,'...')
    conta =  +e +i+p3
 
    return conta