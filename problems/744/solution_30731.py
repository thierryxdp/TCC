# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que reparte a string ao meio e adiciona o 
    caractere(#) no início, meio e final, respectivamente da
    string'''
    meio=len(s)//2
    return '#'+s[0:meio]+'#'+s[meio:]+'#'