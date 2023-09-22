# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string e insere o caractere '#' 
    no inicio, meio e fim; string -> string'''
    comp = len(s)
    return str('#') + s[0:(comp//2)] + str('#') + s[(comp//2):] + str('#')