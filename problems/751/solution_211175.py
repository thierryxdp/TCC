# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que retorna a quantidade de palavras existentes em uma frase;
    str -> int"""
    separa = str.split(frase)
    return len(separa)