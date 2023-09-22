# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Coloca uma hashtag no inicio, meio e fim da string
    '''
    ini_string = s[:len(s)//2]
    fin_string = s[len(s)//2:]
    return '#' + ini_string + '#' + fin_string + '#'