def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    consoante='bcdfghjklmnpqrstvwxyz'
    c_maiuscula=''
    tudo_upper=str.upper(frase)
    while 'A' or 'E' or 'I' or 'O' or 'U' in tudo_upper:
        c_maiuscula=str.replace(tudo_upper,'AEIOU','aeiou')
        
    return c_maiuscula