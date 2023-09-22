# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Função que dada uma frase, retorna ao número de palavras da frase,str->list"""
    frase_1=frase.split(" ")
    return len(frase_1)