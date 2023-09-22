def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    consoante='bcdfghjklmnpqrstvwxyz'
    c_maiuscula=''
    str.upper(frase)
    
    while frase in 'AEIOU':
        c_maiuscula=str.replace(frase,'AEIOU','aeiou')    
    return frase