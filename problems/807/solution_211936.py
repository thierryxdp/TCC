def conta_frases(string):
    '''conta o nº de frases que aparecem nesse texto
    string -> int'''
    string = str.split(string, "!")
    string = str.split(string, "...")
    string = str.split(string, ".")
    string = str.split(string, "?")
    return len(string)