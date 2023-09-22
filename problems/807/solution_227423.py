def conta_frases(texto):
    '''diz quantas frases existem em um texto de entrada str->int'''
    return len(texto.split('.','!','?','...'))