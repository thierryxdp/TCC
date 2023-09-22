# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Função que insere o caractere "#" no ínicio, no meio, e no final
    na string dada.
    Parâmetros:
    	s: Str
    Saída:
    	Str
    """
    metade = int(len(s)/2)
    return '#' + s[:metade] + '#' + s[metade:] + '#'