# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que, dada uma string, retorna a mesma 
    string porém com o caractere '#' no início, no 
    meio e no final da string
    str -> str'''
    x = len(s)//2
    return '#' + s[0:x] + '#' + s[x:] + '#'