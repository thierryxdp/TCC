def conta_frases(s):
	char = ['.','!','?','...']
    sentences = str.replace(s,"...",".")
    sentences = str.count(s,char[0])
	sentences = sentences + str.count(s,char[1])
	sentences = sentences + str.count(s,char[2])
    sentences = sentences + str.count(s,char[3])
    return sentences