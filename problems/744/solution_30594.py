# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e retorna inserindo um '#'no inicio, meio e final
	str -> str"""
    
    num = len(s)
    
    return '#' + s[0:num//2] + '#' + s[num//2:] + '#'