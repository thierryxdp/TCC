def conta_frases(texto):
    '''Função que conta o número de frases presentes em um texto;
    string -> int'''
    s=texto
    x=str.split(s,('.','!','?','...'))
    return len(x)