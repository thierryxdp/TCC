# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Insere o caractere '#' no início, no meio e no final de uma string.
       Entrada: str
       Saída: str
       """
    m = int(len(s)/2)
	return "#"+s[:m]+"#"+s[m:]+"#"