def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    consoante='bcdfghjklmnpqrstvwxyz'
    c_maiuscula=''
    while frase in consoante:
        c_maiscula=c_maiuscula+str.replace(frase,consoante,str.upper(consoante))
     
    return c_maiscula