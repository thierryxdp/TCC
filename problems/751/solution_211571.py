# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "função com a intenção de ver a quantidade de palavras em uma frase usando a funçao split"
    contagem= len(frase.split())
    return contagem