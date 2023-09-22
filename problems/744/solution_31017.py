# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string s e retorna uma outra string
    igual a s, mas com o caractere # no início, no meio e no final 
    da string; str->str'''
    return '#'+s[0:(len(s)//2)]+'#'+s[len(s)//2:]+'#'