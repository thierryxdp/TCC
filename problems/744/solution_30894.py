# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função retorna a string com # em seu início, meio e fim;
    str -> str'''
    ini = s[:len(s)//2]
    fim = s[len(s)//2:]
    return '#' + ini + '#' + fim + '#'