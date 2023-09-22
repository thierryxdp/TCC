def filtra_pares(x):
    '''funcao que filtra os numeros pares de uma tupla,retornando uma nova tupla apenas com os numeros pares;
    tuple -> tuple'''
    tupla = ()
    if x[0]%2==0:
        tupla = tupla + (x[0],)
    if x[1]%2==0:
        tupla = tupla + (x[1],)
    if x[2]%2==0:
        tupla = tupla + (x[2],)
    if x[3]%2==0:
        tupla = tupla + (x[3],)
    if x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0:
        tupla = tupla + (x[0],) + (x[1],) + (x[2],) + (x[3],)
    if x[0]%2==0 and x[1]%2==0:
        tupla =tupla + (x[0],) + (x[1],)
    if x[0]%2==0 and x[2]%2==0:
        tupla = tupla + (x[0],) + (x[2],)
    if x[0]%2==0 and x[3]%2==0:
        tupla =  + (x[0],) + (x[3],)
    if x[0]%2==0 and x[2]%2==0 and x[3]%2==0:
        tupla = tupla + (x[0],) + (x[2],) + (x[3],)
    if x[2]%2==0 and x[3]%2==0:
        tupla = tupla + (x[2],) + (x[3],)
       
    else:
        return tupla