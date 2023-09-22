# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que ao receber uma frase, retorna o número de palavras dessa frase;
    str -> int"""
    x = str.split(frase)
    return len(x)