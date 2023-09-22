# Questão 5 Laboratório 5 Ana Célia Siqueira DRE 119194061 
# lista = list.reverse(lista)
def inverte_phrase(phrase):
    """funcao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa."""
    lista = str.split(phrase)
    lista.reverse()
    phrase = str.join(" ", lista)
    return phrase