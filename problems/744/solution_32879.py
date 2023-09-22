def hashtag(s):
    """Função que retorna o caractere # no início, meio e o final da string inserida. str-> str""""
    s1 = s[:len(s)//2]
	s2 = s[len(s)//2:]
    return "#" + str(s1) + "#" + str(s2) + "#"