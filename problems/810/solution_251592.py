def retira_pontuacao(frase):
    ls = [("...", " "), (".", " "), ("!", " "), ("?", " "), (",", " "), ("-", " "), (":", " "), (";", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase

def inverte(palavra):
  '''Calcule e retorne uma função que inverte a frase''' 
 r = []
    
 str = "LearnPython"

reversed_string=''.join(reversed(str))

return ("The Reversed String is", reversed_string)