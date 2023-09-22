# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna uma string com uma # inserida no início, meio e final dela.'''
    pp = s[:len(s)//2]
    sp = s[len(s)//2:]
    s = "#" + pp + "#" + sp + "#"
    return s