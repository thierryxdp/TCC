# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def imparpar(i):
    """Função que define se i é par ou ímpar"""
    if i%2=0:
        return 'par'
    else:
        return 'ímpar'
    
def hashtag(s):
    """Função que insere # no início, no meio e no fim de uma string s
    str -> str"""
    i = len(s)
    if imparpar(i)='par':
        return '#' + s[:i/2] + '#' + s[i/2:] + '#'
    else:
        return '#' + s[:(i-1)/2] + '#' + s[(i-1)/2:] + '#'