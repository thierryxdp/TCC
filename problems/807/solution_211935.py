def conta_frases(string):
    '''conta o nº de frases que aparecem nesse texto
    string -> int'''
    string = str.split(frase, "!")
    string = str.split(frase, "...")
    string = str.split(frase, ".")
    string = str.split(frase, "?")
    return len(string)