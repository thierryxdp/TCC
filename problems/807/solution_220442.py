def retirapontuacao(frase):
    """retira a pontuação de uma dada frase"""
    frase = frase.replace(' ','x')
    frase = frase.replace('?','? ')
    frase = frase.replace('.','. ')
    frase = frase.replace('!','! ')
    frase = frase.replace('...','...')
    frase = frase.replace(',',',  ')
    return frase
def conta_frases(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    frase = retirapontuacao(frase)
    lista = frase.split()
    return len(lista)