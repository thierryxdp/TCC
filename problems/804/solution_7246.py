#Essa funcao filtra os elementos pares e os retorna em uma tupla
#int int int int --> tupla(int)
def filtra_pares(a,b,c,d):
    tupla = (a,b,c,d)
    resultado = ()
    if tupla[0]%2 == 0:
        return resultado + a
    if tupla[1]%2 == 0:
        return resultado + b
    if tupla[2]%2 == 0:
        return resultado + c
    if tupla[3]%2 == 0:
        return resultado + d