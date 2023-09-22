def inverte(frases):
    """funcao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa."""
    
    lista = frases.split(' ')
    frases.lower()
    lista.reverse()
    for caracteres in "-,:;,.~^*&¨%$#@!":
        frases = frases.replace(caracteres," ")
    return str.join(' ', lista)