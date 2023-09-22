# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao ue recebe uma string e insire 
    o caractere ”#” no início, no meio e no final dela.'''
    return '#'+s[0:(len(s)//2)+1]+'#'+s[(len(s)//2)+1:]+'#'