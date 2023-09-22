# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dado uma string, retorna a mesma com 3 #, uma no comeco,
    uma no meio e uma no final.
    str-> str'''
    metade = int(len(s)//2)
	    
    parte1 = s[0:metade]
    parte2 = s[metade::]
    
    a = "#"
    return a + parte1 + a + parte2 + a