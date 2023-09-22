# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Conta a quantidade de palavras em uma frase, str->int"""
    frase = str.split(frase)
    x = list.count (' ',frase[0:])
    y = list.count (',',frase[0:])
    z = list.count ('.',frase[0:])
    w = list.count (';',frase[0:])
    return len(frase) - y - x - z - w