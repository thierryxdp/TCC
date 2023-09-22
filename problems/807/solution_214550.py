def conta_frases(texto):
    '''Função que recebe um texto e retorna o número de frases contido nele; str -> int'''
    texto = texto.replace("...", "@")
    
    result = texto.count(".") + texto.count("!") + texto.count("?") + texto.count("@")
    
    return result