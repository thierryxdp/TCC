# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    frase = list (frase)
    x = list.count (' ',frase[0:])
    y = list.count (',',frase[0:])
    z = list.count ('.',frase[0:])
    w = list.count (';',frase[0:])
    return len(frase) - y - x - z - w