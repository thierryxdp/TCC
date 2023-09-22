def filtra_pares(b):
    '''Função que retorna uma nova tupla contendo apenas
    os elementos pares da tupla original, na mesma ordem em que
    se encontravam.
    a=int,b=int,c=int,d=int->tuple'''
    x=()
    if b[0]%2==0:
      x= x+(b[0],)
    if b[1]%2==0:
      x= x+(b[1],)
    if b[2]%2==0:
      x= x+(b[2],)
    if b[3]%2==0:
      x= x+(b[3],)
    return x