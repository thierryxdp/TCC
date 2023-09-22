# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string e insere # no início, 
    no meio e no final dela
    str -> str'''
    if len(s)%2==0 :
        ponto = len(s)//2
    else:
        ponto=(len(s)-1)//2
    return  '#' + s[:ponto] + '#' + s[ponto:] + '#'