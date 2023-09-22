# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A partir da frase de entrada retorna o numero de palavras
    dessa frase
    string -> int"""
    frase_pura = str.strip(frase)
    return int(str.count(frase_pura,' '))+int(1)