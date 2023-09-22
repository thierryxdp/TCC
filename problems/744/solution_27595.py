# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(stri_s):
    """esta funcao coloca # no inicio e final da string"""
    meio = len(stri_s) / 2
    	return "#" + stri_s[:meio] + "#" + stri_s[meio:] + "#"