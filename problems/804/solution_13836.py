#Start your python function here
def PAR(x):
    """Função que, dado de entrada um número inteiro,
    retorna o booleano True, caso esse número seja par.
    int -> bool"""
    return (x%2) == 0

def filtra_pares(t):
    """Essa função recebe de entrada uma tupla com 4 números
    inteiros e retorna uma nova tupla contendo apenas 
    os que são pares, na ordem em que aparecem.
    tup(int) -> tup(int)"""
    pares = ()
    if PAR(t[0]):
        pares = pares + (t[0],)
    if PAR(t[1]):
        pares = pares + (t[1],)
    if PAR(t[2]):
        pares = pares + (t[2],)
    if PAR(t[3]):
        pares = pares + (t[3],)
    return pares

#Casos de teste
#filtra_pares((2,7,8,34)) == (2, 8, 34)
#filtra_pares((200,-2,31,-25)) == (200, -2)
#filtra_pares((531,-299,310,-252)) == (310, -252)
#filtra_pares((6,52,-38,24)) == (6, 52, -38, 24)