import re
def conta_frases(frase):
    return len(re.split('. . . |. ', frase))