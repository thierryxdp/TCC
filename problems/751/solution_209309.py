# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ dado uma frase retorna o numero de palavras 
    pertencente a essa frase
    str -> int"""
    separado = frase.split()
    return len(separado)