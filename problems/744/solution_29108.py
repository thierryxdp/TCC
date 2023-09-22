# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Retorna a string s com '#' no inicio, no meio e no fim
    	str -> str
        Explicação: calcula a posição media da string e arredonda para baixo, e concatena um '#' nas posições corretas'''
    m = len(s)//2
    ret = '#' + s[:m] + '#' + s[m:] + '#'
    return ret