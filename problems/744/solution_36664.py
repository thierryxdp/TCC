# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funçao que recebe uma string e insere o caractere # no inicio, no meio e no final
    str-->str'''
    	s= "#" + s[:len(s)//2] + "#" + S[len(s)//2:]
    return s