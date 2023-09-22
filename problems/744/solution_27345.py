# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """calcula e retorna uma função que recebe uma string e insere o 
    caractere # no início, no meio e no final dela - str -> str"""
    s1=s[0:int(len(s)/2)]
    s2=s[int(len(s)/2):]
    return '#'+s1+'#'+s2+'#'