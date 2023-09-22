#Questão 1
def quant_palavras(frase):
    """função que dada uma frase, retorna
o numero de palavras da frase
ex: >>>palavras('Leo Leo') - 2
str -> int"""
    x = str.split(frase) #função split para retirar o espaços
    return len(x) #transformado em lista, utiliza-se a função len para contagem