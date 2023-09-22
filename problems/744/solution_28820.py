# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função recebe uma string e coloca o caractere "#"
	no início, no meio e no final dela;
	str -> str"""
	metade = math.floor(len(s)/2)
    return '#'+s[:metade]+"#"+[metade:]