def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."
    lista = str.split(frase)
    lista2 = lista.lower()
    fraseInvertida = str.join("",lista2)
    return fraseInvertida