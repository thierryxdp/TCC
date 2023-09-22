def pares_novos(n):
    '''retorna true se for par, false se impar
    int ou float->bool''';
    return n%2==0
def filtra_pares(p):
    pares=()
    if pares_novos(p[0]):
        pares=pares+(p[0],)
    if pares_novos(p[1]):
        pares=pares+(p[1],)
    if pares_novos(p[2]):
        pares=pares+(p[2],)
    if pares_novos(p[3]):
        pares=pares+(p[3],)
        return pares