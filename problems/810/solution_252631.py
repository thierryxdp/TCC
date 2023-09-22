def inverte(frase):
    """funcao que dada uma frase retorna uma outra que contenha as mesmas palavras da frase
    inicial, porem na ordem inversa"""
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, "?", "")
    frase = str.replace(frase, "!", "")
    frase = str.replace(frase, ".", "")
    frase = str.replace(frase, ";", "")
    frase = str.replace(frase, ",", "")
    frase = str.lower(frase)
    frase = str.split(frase)
 	frase = list.reverse(frase)
    return frase