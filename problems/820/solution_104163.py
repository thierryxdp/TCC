def posLetra(x,y,z):
    """A função retorna em qual indice está a letra que é repetida durante a string em determinado
    numero de ocorrencia, caso a string tenha menos letras do que o numero de ocorrencia ela ira
    retornar -1
    str + str + int --> int"""
    A = str.count(x, y)
    for letra in x:
        if A<z:
            return -1
        elif letra == y:
            return x.find(y)