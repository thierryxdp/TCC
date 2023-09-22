#Questao 2
def conta_frases(frases):
    '''
Funcao que conte o número de frases que 
aparecem neste texto.
string -> int
    '''
    punct = string.punctuation
    
    for (. ! ? ...) in punct:
    frases = frases.replace((. ! ? ...), "")
    return (frases)