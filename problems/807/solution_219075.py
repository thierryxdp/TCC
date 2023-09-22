def conta_frases(s):
    char = ['.','!','?','...']
    if char[0] in s:
        sentences = str.count(s,char[0])
   
    return len(str(sentences))