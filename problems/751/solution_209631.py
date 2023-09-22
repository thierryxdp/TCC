# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    'retorna a quantidade de palavras em uma frase'
    'str -> int'
    x=frase.split()
    y=x.count(' ')
    return len(x)-y