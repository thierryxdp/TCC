# recebe uma tupla com quatro elementos inteiros como parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
# quatro elementos inteiros a, b, c, d
# int, int, int, int --> tup
def filtra_pares(inteiros):
    a,b,c,d = inteiros
    retorno = ()
    if int(inteiros[0])%2==0:
        retorno = retorno +(inteiros[0],)
    if int(inteiros[1])%2==0:
        retorno = retorno +(inteiros[1],)
    if int(inteiros[2])%2==0:
        retorno = retorno +(inteiros[2],)
    if int(inteiros[3])%2==0:
        retorno = retorno +(inteiros[3],)
    return retorno