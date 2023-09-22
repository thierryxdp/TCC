def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."
    lista1 = str.split(frase)
    lista2 = lista1.lower(frase)
    fraseInvertida = str.join("",lista2)
    return fraseInvertida