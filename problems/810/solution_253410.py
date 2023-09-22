def inverte(texto):
    """função que dada uma frase, retorna uma outra frase com as mesmas palavras da frase de entrada na ordem inversa, sem pontuação e sem letras maiúsculas 
    string -> string"""
    for x in '.:;-,?!':
        texto=texto.replace(x,' ')
    texto1=str.split(texto)
    list.reverse(texto1)
    texto_invertido=str.join(',', texto1)
    return str.lower(texto_invertido.replace(x, ' '))