def filtra_pares(tupla):
    '''função que retorna uma tupla apenas com elementos pares. Sendo ela contendo 4 elementos''' 
    tupla_par= ()
    if tupla[0]%2==0:
        tupla_par=tupla_par+(tupla[0],)
    if tupla[1]%2==0:
        tupla_par=tupla_par+(tupla[1],)
    if tupla[2]%2==0:
        tupla_par=tupla_par+(tupla[2],)
    if tupla[3]%2==0:
        tupla_par=tupla_par+(tupla[3],)
        return tupla_par
        else:
        return ()