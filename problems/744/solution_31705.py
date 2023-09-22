# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Reecebe uma string e insere o caractere "#" no inicio, meio e fim da string com o caractere inserido; str->str."""
	tamanho_str=len(s)
    meio=(tamanho_str//2)
    s_hashtag="#"+s[0:meio]+"#"+s[meio:]
	return s_hashtag