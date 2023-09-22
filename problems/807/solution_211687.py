def conta_frases(string):
    '''dado um texto, retona o numero de frases presentes no mesmo
    str -> int'''
    return len(str.split(string, "!" or "." or "..." or "?"))