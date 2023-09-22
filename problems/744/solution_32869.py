# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """"""
    s1 = s[:len(s)//2]
	s2 = s[len(s)//2:]
    sn = str(s1 + s2)
    return "#" + "#".join(sn) + "#"