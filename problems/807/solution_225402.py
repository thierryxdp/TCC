import re
def conta_frases(entrada):
    return len(re.findall(r'\w+', entrada))