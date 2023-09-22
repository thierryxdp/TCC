def conta_frases(texto):
    "dado um texto, retorna o numero de palavras dela str -> str"
    texto2 = texto.split('.')
    texto3 = texto2.split('!')
    texto4 = texto3.split('?')
    texto5 = texto4.split('...')
    return len(texto5)