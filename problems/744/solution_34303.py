def hashtag(s):
# str->str
# coloca "#" no final, inicio e meio de uma string dada
	return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"