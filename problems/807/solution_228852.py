def conta_frases(texto):
    '''
    Funçao que recebe um texto e conta o numero de frases que ele tem
    str -> int
    '''
    t1= str.split(texto,'...')
    T1= str.join(t1[1],t2[0])
    t2= str.split(T1,'.')
    T2= str.join(t2[1],t2[0])
    t3= str.split(T2,'?')
    T3= str.join(t3[1],t3[0])
    t4= str.split(T3,'!')
    T4= str.join(t4[1],t4[0])
    return T4