# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """conta o número de palavras contando os espaços como caracteres-->str , int"""
    frase= frase.strip(" ")
    return str.count(frase," ") + 1