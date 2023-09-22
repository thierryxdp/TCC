# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Esta função recebe uma string e retorna outra string, contendo a string fornecida com o caractere '#' inserido no
    começo, meio e fim dela.
    
    Parametros
    ----------
    s (string) : string
    '''
    l = round(len(s))
    return '#' + s[:int(l/2)] + '#' + s[int(l/2):] + '#'