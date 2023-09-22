import re 
def conta_frases(texto):
    '''conta quantas frases existem em um texto, onde
    as frases terminam em apenas '.','...','?' e '!';
    string -> int'''
    return len(re.split(.!?...,texto))