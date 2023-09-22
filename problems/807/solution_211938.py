def conta_frases(string):
    '''conta o nº de frases que aparecem nesse texto
    string -> int'''
    stringNova = str.split(string, "!")
    stringNova = str.split(string, "...")
    stringNova = str.split(string, ".")
    stringNova = str.split(string, "?")
    stringNova = str.split(string," ")
    return len(stringNova)