# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Função que recebe uma string e retorna a string com # no inicio, meio e fim 
        str -> str
    '''
    if (len(s)%2) == 0:
        return '#' + s[:(len(s)//2)] + "#" + s[(len(s)//2)+1:] + '#'
    else:
        return '#' + s[:(len(s)//2)] + "#" + s[(len(s)//2)+1:] + '#'