# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que retorna a string s com um hashtag no inicio, meio e fim;
    	str -> str
    """
    metade_string = len(s) // 2
    return "#" + s[0: metade_string] + "#" + s[metade_string + 1: len(s)] + "#"