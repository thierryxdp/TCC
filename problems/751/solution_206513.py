# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que recebe uma string e retorna o número de palavras da frase"""
    frase = frase.split()
    return len(frase)