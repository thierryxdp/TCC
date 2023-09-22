# Questão 5 Laboratório 5 Ana Célia Siqueira DRE 119194061 
def inv_phrase(phrase):
    """funcao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa."""
    lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return phrase