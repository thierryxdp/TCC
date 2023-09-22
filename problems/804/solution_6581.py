#Start your python function here
def filtra_pares(a):
    '''Função que receba de parâmetro uma tupla de 4 elementos e devolva 
    	apenas os elementos pares da tupla.
        tupla -->tupla.'''
    b=()
    if (a[0]%2==0):
        b=b+(a[0],)
    if(a [1]%2==0):
        b=b+(a[1],)
    elif (a[2]%2==0):
        b=b+(a[2],)
    elif (a[3]%2==0):
        b=b+(a[3],)
    return b