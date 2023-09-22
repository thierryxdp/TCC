# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    frase = retirapontuacao(frase)
    lista = s.split()
    return len(lista)
def retirapontuacao(frase):
    """retira pontuação de dada frase"""
    frase = frase.replace('!',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = farse.replace(';',' ')