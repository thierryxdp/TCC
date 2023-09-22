def conta_frase(texto):
    '''funçao que conta o numero de frases que aparecem em um texto,dado um texto de entrada; str->int'''
    return str.count(texto,"!")+str.count(texto,"?")+str.count(texto,".")+str.count(texto,",")