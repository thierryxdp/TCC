# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Receba uma string e insira o caractere ”#” no inicio, no meio
	e no final dela;
    string -> string"""
    meio = len(s) // 2
    return "#" + s[0:meio] + "#" + s[meio:] + "#"