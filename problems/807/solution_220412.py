def retirapontuacao(frase):
    """retira a pontuação de uma dada frase"""
    frase = frase.replace(' ','x')
 
    return frase
def conta_frases(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista = frase.split()
    return len(lista)