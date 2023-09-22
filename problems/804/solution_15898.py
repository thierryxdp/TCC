def filtra_pares(numeros):
    """dado uma sequencia de quatro numeros inteiros retorna apenas
    pares. entra os quatro numeros em tupla; tupla(int,int,int,int)->
    tupla(int) a quantidade de elementos da tupla depende da quantidade
    de numeros pares dados na entrada"""
    tuplafinal=()
    if numeros[0]%2==0:
        tuplafinal=(numeros[0],)
    if numeros[1]%2==0:
        tupla1=(numeros[1],)
        tuplafinal=tuplafinal+tupla1
    if numeros[2]%2==0:
        tupla2=(numeros[2],)
        tuplafinal=tuplafinal+tupla2
    if numeros[3]%2==0:
        tupla3=(numeros[3],)
        tuplafinal=tuplafinal+tupla3
    return tuplafinal