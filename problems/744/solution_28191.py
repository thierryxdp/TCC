# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebia uma string e devolva o caractere # no início,
    	no meio e no final.
        str-->str'''
    return '#' s[0:len(s)//2]+'#'+s[len(s)//2:len(s)]+'#'