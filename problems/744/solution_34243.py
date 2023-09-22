# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna uma palavra com a string(#) no início meio e fim
       str --> str'''
    comp = len(s) // 2 
    nova_palavra = '#' + s[:comp] + '#' + s[comp :] + '#'
    return nova_palavra