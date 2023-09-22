# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna o numero de palavras de uma frase, dado uma frase
       str-> int"""
    return len(str.join('',(str.split(frase, ' '))))