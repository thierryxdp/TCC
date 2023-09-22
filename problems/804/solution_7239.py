#Essa funcao filtra os elementos pares e os retorna em uma tupla
#int int int int --> tupla(int)
def filtra_pares(abcd):
    tupla = (a,b,c,d)
    resultado = ()
    if tupla[0]%2 == 0:
        resultado = resultado + a
    if tupla[1]%2 == 0:
        resultado = resultado + b
    if tupla[2]%2 == 0:
        resultado = resultado + c
    if tupla[3]%2 == 0:
        resultado = resultado + d
        return resultado