def uppCons2(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    i=0
    consoante='bcdfghjklmnpqrstvwxyz'
    c_maiuscula=''
    while len(frase)>0:
        if frase in consoante:
            frase=str.replace(frase,consoante,str.upper(consoante))
    i=i+1    
    return frase