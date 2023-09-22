def inverte(texto):
    '''
    Funçao que recebe um texto e retorna ele invertido
    str -> str
    '''
    t1=str.split(texto,'...')
    T1=str.join(' ',t1)
    t2=str.split(T1,'?')
    T2=str.join(' ',t2)
    t3=str.split(T2,'!')
    T3=str.join(' ',t3)
    t4=str.split(T3,'.')
    T4=str.join(' ',t4)
    t5=str.split(T4,'-')
    T5=str.join(' ',t5)
    t6=str.split(T5,',')
    T6=str.join(' ',t6)
    t7=str.split(T6,':')
    T7=str.join(' ',t7)
    t8=str.split(T7,';')
    T8=str.join(' ',t8)
    
    T9=str.lower(T8)
    T10=str.split(T9)
    t11=str.join(' ',T10)
    return t11