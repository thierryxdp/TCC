# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase, retorna o número de palavras quem ela contém;
    str -> int"""
    palavras = str.split(frase)
    quantidade = len(palavras)
    return quantidade