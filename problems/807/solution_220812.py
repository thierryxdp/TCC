def conta_frases (texto: str)-> int:
    '''retorna o número de frases presentes no texto dado'''
    texto= str.replace(texto,'...' , '.')
    texto= str.replace(texto, '!' , '.')
    texto= str.replace(texto, '?' , '.')
    frases= str.split (texto, '.')
    return len(frases)