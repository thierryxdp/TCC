def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;string-->int"""
    f='frase.'
    if '.' not in '...':
           return True       
    return len(f.count('.','!','?','...'))