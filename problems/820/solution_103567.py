def posLetra(string, letra, n):
   ''' 
   '''
    qnt_letras= str.count(string, letra)    
    
    
    if letras> n:
        return -1
    
    i=0
    p=0
    while i<len(string):
        p= str.index(string, letra, n)
        i=p+1
        i+=1 
return p