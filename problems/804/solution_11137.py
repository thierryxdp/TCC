def filtra_pares(tup):
    """Recebe uma tupla com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam> Tupla--> Tupla"""
    
    
    a = (tup[0]%2==0)
     
    b =(tup[1]%2==0)
     
    c = (tup[2]%2==0)
        
    d =(tup[3]%2==0)
    
    if  (a,b,c,d)= (True): 
        return 'a'+'b'+'c'+'d'