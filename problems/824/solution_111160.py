def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    i=0
    consoant='bcdfghjklmnpqrstvwxyz' 
    nova_frase=''
    while i<len(frase):
        if frase[i] in consoant:
            str.partition(frase,consoant)
            nova_frase = str.upper(consoant)
            
            
        i = i + 1    
    return nova_frase