# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que pega o valor s de entrada e retorna no incio, meio e fim o # nela 
       str,str→str'''
	s= '#'+s+'#'
    meio= len(s)//2
    s= s[:meio] + '#' + s[meio:]
    return s