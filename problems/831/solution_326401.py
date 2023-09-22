def lingua_p(palavra):
    n=0
    nova=palavra
    lista=["a","e","i","o","u"]
    for i in palavra:
        if palavra[n] in lista:
            nova=str.replace(nova,nova[n],nova[n]+"p")
            list.remove(lista,palavra[n])
        n=n+1
    return nova