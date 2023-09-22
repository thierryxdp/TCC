def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."   
    lista = str.split(frase)
    lista.lower()
    frase = str.join(" ", lista)
    return frase