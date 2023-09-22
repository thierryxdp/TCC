# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s) - len(s)//2
	if len(s) % 2 == 0:
        return '#' + str(s)[0 : x] + '#' + str(s)[x :] + '#'
    if len(s) % 2 != 0:
        return '#' + str(s)[0 : x - 1] + '#' + str(s)[x :] + '#'