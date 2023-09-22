def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    c_maiuscula=''
    while letter in frase:
        if letter in not 'aeiouAEIOU':
        c_maiuscula=c+_maiuscula+letter.upper()    
    return c_maiuscula