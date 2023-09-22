# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    a = list (frase)
    x = str.count (' ',a[0:])
    y = str.count (',',a[0:])
    z = str.count ('.',a[0:])
    w = str.count (';',a[0:])
    return len(a) - y - x - z - w