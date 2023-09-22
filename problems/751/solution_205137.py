# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "Faca uma funcao que dada uma frase, retorne o numero de palavras da frase."
    l = str.split(frase,' ')
    n = len(l)
    if l[0] == '':
        n -=1
    if l[len(l)-1] == '':
        n -=1
    return n