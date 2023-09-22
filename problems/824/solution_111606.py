def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    i=0
    consoante=''
    consoante=consoante+'b'
    consoante=consoante+'c'
    consoante=consoante+'d'
    consoante=consoante+'f'
    consoante=consoante+'g'
    consoante=consoante+'h'
    consoante=consoante+'j'
    consoante=consoante+'k'
    consoante=consoante+'l'
    consoante=consoante+'m'
    consoante=consoante+'n'
    consoante=consoante+'p'
    consoante=consoante+'q'
    consoante=consoante+'r'
    consoante=consoante+'s'
    consoante=consoante+'t'
    consoante=consoante+'v'
    consoante=consoante+'x'
    consoante=consoante+'y'
    consoante=consoante+'z'
    
    
    while frase in consoante:
        mconsoante=str.upper(consoante)
        str.replace(frase,consoante,mconsoante)
        
        
    i=i+1    
    return frase