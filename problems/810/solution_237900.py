def inverte_phrase(phrase):
    """funcão que dada uma frase retorna uma frase diferente com as mesmas palavras da 
    anterior"""
    lista = str.split(phrase)
    lista.reverse()
    phrase = str.join(" ", lista)
    return phrase