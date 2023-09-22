# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que entra uma string e retorna string com os caracteres # no início,meio e fim"""
	inicio = s[:len(s)//2]
	fim = s[len(s)//2:]
 	return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] +'#'