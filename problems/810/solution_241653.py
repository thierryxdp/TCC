def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."   
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    fraseInvertida = frase.lower()
    return fraseInvertida