# 4) Função hashtag.

def metade(string):
    '''dada uma string, retorna o número que representa a posição do meio da string.
    str -> int'''
    return len(string)//2

def hashtag(string):
    '''dada uma string, retorna ela com # em seu inicio, meio e fim.
    str -> str'''
    meio = substitui(string, ("#" + string[metade(string)]), metade(string))
    hashtag = "#" + meio + "#"
    return hashtag