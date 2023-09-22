" A funcao intercala duas listas com tres numeros quaisquer"
"lista1= list(int, int, int) lista2= list(int, int, int)"
def intercala(lista1, lista2):
    """Intercala duas listas com tres numeros quaisquer
    tais que essas listas dao a entrada e retorna uma lista
    inedita"""
    return [lista1[0], lista2[0], lista1[1], lista2[1],lista1[2], lista2[2]]