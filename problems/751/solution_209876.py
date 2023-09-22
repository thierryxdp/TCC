# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que conta quantas palavras estão dentro de uma frase, dada a frase comop entrada;
    str -> int"""
    num_palavras = str.split(frase)
    return len(num_palavras)