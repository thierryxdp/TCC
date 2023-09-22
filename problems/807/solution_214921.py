def conta_frases(s):
    char = ['.','!','?','...']
    char_replace = ['!','?','...']
    for char in char_replace:
        s = s.replace(char,'.')
    sentences = s.split('.')
    sentences = sentences[:-1]
    return len(sentences)