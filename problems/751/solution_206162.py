# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que recebe uma frase e retorna o numero de palavras da frase"""
    quantidade = str.split(frase)
    return len(quantidade)