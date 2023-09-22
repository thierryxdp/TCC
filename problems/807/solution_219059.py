def conta_frases(s):
    char = ['.','!','?','...']
    s = s.replace(char,'.')
    sentences = s.split('.')
    sentences = sentences[:-1]
    return len(sentences)