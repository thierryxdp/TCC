def conta_frases(s):
    char = ['.','!','?','...']
    if char[0] in s:
        sentences = str.count(s,char[0])
    elif char[1] in s:
        sentences = sentences + str.count(s,char[1])
    elif char[2] in s:
        sentences = sentences + str.count(s,char[1]) + str.count(s,char[2]) 
    elif char[3] in s:
        sentences = sentences + str.count(s,char[1]) + str.count(s,char[2]) + str.count(s,char[3])
    return len(str(sentences))