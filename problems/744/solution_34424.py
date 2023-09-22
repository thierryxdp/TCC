# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''a função recebe uma string s e insere '#' no inicio, meio e fim da string
    casos de teste:
    hashtag('abcd') == '#ab#cd#'
    hashtag('naomy')== '#na#omy#')
    '''
    string = s
    divisao = len(s)//2
    x = string[:divisao]+'#'
    y = string[divisao:]

    return '#'+x+y+'#'