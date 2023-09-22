def conta_frases(frase):
    '''Função que conta o número de frases presentes um um texto;
    string -> string'''
    for char in "!?":
        frase = frase.replace(char, ".")
    return len(str.split(frase, ". "))