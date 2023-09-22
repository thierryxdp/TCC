# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função chamada hashtag que receba uma string e insira o caractere ”#” no in ́ıcio, no meio
e no final dela.'''
    
    m = (len(s)//2)
    return '#'+s[:m]+'#'+s[m:]+'#'