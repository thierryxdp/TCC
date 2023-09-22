# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma strig e retorna a string com uma "#" no início, no meio e no final dela; str-> str'''
	metade=len(s)//2
    return s[:metade]+'#'+s[metade:]