def filtra_pares(tup):
    """Recebe uma tupla com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam> Tupla--> Tupla"""
    
    A,B,C,D=tup
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    tuplapares=()
    if (a%2==0):
        tuplapares = tuplapares+(a,)          
    if (a%2==0):
        tuplapares = tuplapares+(b,)
   
    if (a%2==0):
        tuplapares = tuplapares+(c,)
       
    if (a%2==0):
        tuplapares = tuplapares+(d,)
        
        return tuplapares