# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que retorna a string passada como parametro com hashtags no inicio, no meio e no fim da palavra.
       string -> string'''
    if (len(s)%2 == 0):
        meiopalavra = int(len(s)/2)
    else:
        meiopalavra = len(s)//2
    
    return '#' + s[:meiopalavra] + '#' + s[meiopalavra:] + '#'