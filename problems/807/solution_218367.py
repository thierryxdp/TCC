import re
def conta_frases(frase):
    
    pontuacao= re.split('\.|\!|\?|\.\.\.',frase)
    
    print(len(pontuacao))