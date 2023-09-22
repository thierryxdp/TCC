# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funçao que dada uma frase retorna o numero de palavras da frase
    str-->int"""
    if " " in frase:
        x = split(frase)
        list.remove(x, "")
        return len(frase)
    else:
        return len(frase)