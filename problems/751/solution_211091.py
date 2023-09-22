# Função que divide uma string dada por cada espaço e retorna
# a quantidade de itens divididos
# string -> int
def quantidade_palavras(frase):
    x = frase.split()
    return len(x)