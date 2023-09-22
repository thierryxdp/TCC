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
    list1 = frase
    list1.reverse()
    list1.join(list1)
    return list1