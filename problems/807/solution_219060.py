def conta_frases(s):
    char = ['.','!','?','...']
    if char[0] in s:
    	s = s.replace(char,'.')
    if char[1] in s:
    	s = s.replace(char,'.')
    if char[2] in s:
    	s = s.replace(char,'.')
    if char[3] in s:
    	s = s.replace(char,'.')
    sentences = s.split('.')
    sentences = sentences[:-1]
    return len(sentences)