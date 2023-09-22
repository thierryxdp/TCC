# 2) Função de substituição.

def substitui(s, x, i):
    '''dada uma string(s), um cartactere(x) e um inteiro(i), representando o
    caractere a ser substituido, retorna a string modificada.
    str, str, int -> str'''
    inicio = s[:i] 
    meio = str(x)
    fim = s[(i+1):]
    return inicio + meio + fim