def posLetra(frase,l,n):
    """ Função que, dados uma string, uma letra e um número, retorna
    a posição da string onde aquela ocorrencia da letra está
    str, srt, int-> int"""
    ct1 = 0
    ct2=  0

    while ct1 < len(frase):

        if  frase[ct1]  in l:
            ct2 = ct2 + 1
        if ct2==n:  
            return ct1
        if frase.count(l) < n:  
            return  -1 
            
        ct1 = ct1 + 1