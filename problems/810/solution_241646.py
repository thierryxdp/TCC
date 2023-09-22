def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."
    lista = str.split(frase)
    lista2 = str.lower()
    fraseInvertida = str.join("",lista2)
    return fraseInvertida