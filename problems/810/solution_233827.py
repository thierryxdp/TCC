def retira_pontuacao(text):
    return "".join([" " if char in "-.!?," else char for char in text])
def inverte(frase):
    """dada uma frase retorna outra frase que conenha as mesmas palavras na ordem inversa se letras maiusculas e sem pontuação; string-> string"""
    n = retira_pontuacao(frase)
    lista = str.split(n)
    invert = lista[::-1]
    sep = str.lower(str.join(' ', invert))
    return sep