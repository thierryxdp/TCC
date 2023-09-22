# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def retirapontuacao(frase):
    """retira a pontuação dada as palavras"""
    frase = frase.replace('!',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(';',' ')
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    frase = retirapontuacao(frase)
    return frase.split(frase)