def conta_frases(texto):
    """retorna a quantidade de frases em um texto de entrada
    string -> int"""
    a = texto.split('. ')
    b = texto.split('! ') 
    c = texto.split('? ')
    d = texto.split('... ')
    x = a + b + c + d
    return len(x)