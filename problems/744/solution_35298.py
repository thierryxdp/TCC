# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	tamanho = len(s)
    #Se o tamanho for um numero par deve retornar abcd --> #ab#cd#
    centro = tamanho // 2
    buffer = '#' + s[:centro] + '#' + s[centro:] + '#'
        
    return buffer