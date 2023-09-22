#Start your python function here
def filtro(a):
    '''retorna verdadeiro se o numero for par, e falso se for impar
       entrada: int
       saida: bool'''
    return a%2==0
def filtra_pares(a):
    '''recebe uma tupla e cria outra tupla com os elementos pares da primeira
       entrada= tup
       saida= tup'''
    pares=()
    if filtro(a[0]):
        pares= pares+(a[0],)
    if filtro(a[1]):
        pares= pares+(a[1],)
    if filtro(a[2]):
        pares= pares+(a[2],)
    if filtro(a[3]):
        pares= pares+(a[3],)
        return pares 
    else:
        return ()