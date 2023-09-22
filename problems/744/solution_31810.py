# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    '''Funçao que recebe uma string s e insere o caractere #
    no comeco, meio e final da string.'''
    string -> string
    
    n=(len(s)-1)/2
    p1=s[:int(n)+1]
    p2=s[int(n)+1:]
    
    return '#'+p1+'#'+p2+'#'