# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Assim que inserida a frase retorna o numero de palavras desta"""
    f = frase
    n = f.split()
    return len(n)