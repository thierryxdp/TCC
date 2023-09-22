def conta_frases(texto):
    '''
    Funçao que recebe um texto e conta o numero de frases que ele tem
    str -> int
    '''
    t1=str.split(texto,'...')
    T1=str.join('.',t1)
    t2=str.split(T1,'?')
    T2=str.join('.',t2)
    t3=str.split(T2,'!')
    T3=str.join('.',t3)
    t4=str.split(T3,'.')
    
    return len(t4)-1