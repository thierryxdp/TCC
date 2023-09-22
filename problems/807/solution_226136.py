#Questao 2
def conta_frases(frases):
    '''
Funcao que conte o número de frases que 
aparecem neste texto.
string -> int
    '''
    return len (frases.split('. '))