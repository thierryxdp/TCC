def inverte(frase):
    """funcao que dada uma frase retorne uma outra frase que contenha
    as mesmas palavras da frase de entrada na ordem inversa sem letra maiùscula e sem pontuaçao"""
    a = (frase[-1:]) 
    
    lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return frase