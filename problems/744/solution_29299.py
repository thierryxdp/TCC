# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string s e retorna essa mesma com #
    no início, no meio e no final. Ex: abcde --> #ab#cde#
    valor de entrada: str
    valor de saída:str '''
    meiostringpar= len(s)//2
    meiostringimpar=(len(s)+1)//2
    if len(s)%2 == 0:
        return '#'+s[0:meiostringpar]+'#'+s[meiostringpar:]+'#'
    else:
        return '#'+s[0:meiostringimpar]+'#'+s[meiostringimpar:]+'#'