# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que recebe uma string "frase", calcula e retorna o número
    de palavras armazenadas na string.
    str --> int"""
    s = str.split(frase, " ") 
    return len(s)