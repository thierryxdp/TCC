#Start your python function here
def filtra_pares(tupla0):
    '''Dado uma tupla com quatro inteiros a,b,c e d, retorne somente os números pares;
    int,int,int,int -> int,...'''
    tupla1=()
    if tupla0[0]%2==0:
        tupla1=tupla1+(tupla0[0],)
    if tupla0[1]%2==0:
        tupla1=tupla1+(tupla0[1],)
    if tupla0[2]%2==0:
        tupla1=tupla1+(tupla0[2],)
    if tupla0[3]%2==0:
        tupla1=tupla1+(tupla0[3],)
    return tupla1