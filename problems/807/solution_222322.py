#A função recebe um texto(string) e retorna a quantidade de frases presentes.
#txt: texto a ser inserido em string
#str->int
def conta_frases(txt):
    str.split(txt,'.','!','?','...')
    return len(str.split(txt,'.','!','?','...'))