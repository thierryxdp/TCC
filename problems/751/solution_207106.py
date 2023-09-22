# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função recebe uma frase(string) e retorna a sua quantidade de palavras (int)"""
    num = frase.split(' ')
    return len(num)