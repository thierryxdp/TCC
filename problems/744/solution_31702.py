# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Reecebe uma string e insere o caractere "#" no inicio, meio e fim da string com o caractere inserido; str->str."""
	tamanho_str=len(s)
    meio=(tamanho_str//2)+1
    meio_1=meio+1
    s_hashtag="#"+s[0:meio]+"#"+s[meio_1:]
	return s_hashtag