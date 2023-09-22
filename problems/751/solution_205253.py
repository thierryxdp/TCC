# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
"""dada uma frase, que deve vir entre parênteses, a função retorna 
a quantidade de palavras que a frase de entrada possui.
string-->int

Parâmetros
frase: string utilizada como entrada
"""
    return len(str.split(frase))