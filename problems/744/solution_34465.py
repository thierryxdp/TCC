def hashtag(s):
    """Retornar a função, onde o símbolo # seja posto no início, meio e fim da palavra do usuário;str,str,str,str,str=>str"""
	return "#" + s[:len(s)//2]+ "#" + s[len(s)//2] + "#"