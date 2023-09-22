def posLetra(frase,l,n):
    """ Função que, dados uma"""
    ct1 = 0
    ct2=  0

    while ct1 < len(frase):

        if  frase[ct1]  in l:
            ct2 = ct2 + 1
        if ct2==n:  
            return ct1
        if ct2< n:  
            return ct1 -1 
            
        ct1 = ct1 + 1