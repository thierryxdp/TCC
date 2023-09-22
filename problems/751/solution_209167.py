# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número de palavras em uam frase; str -> int"""
    espaco=frase.strip(' ')
    palavras=espaco.split(' ')
    return len(palavras)