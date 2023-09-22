def inverte(frase):
    """função que dada uma frase, retorna uma outra frase com as mesmas palavras da frase de entrada na ordem inversa, sem pontuação e sem letras maiúsculas 
    string -> string"""
    for x in '!?.:;-,':
        frase=frase.replace(x,' ')
    frase2=str.split(frase)
    list.reverse(frase2)
    frase_invertida=str.join(',',frase2)
    return str.lower(frase_invertida.replace(x,' '))