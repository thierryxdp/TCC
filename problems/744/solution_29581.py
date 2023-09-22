# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Função que recebe uma string e insere uma '#' no início,
    no meio e no fim.
    str-> str
    '''
    meio_string= len(s)//2
    a= s[0:meio_string]
    b= s[meio_string:]
    return '#'+a+'#'+b+'#'