def posLetra(string, letra, n):
   ''' 
   '''
    # 
    #if ocorrencias > numeros:
    #    return -1
    letras= str.count(frase, letra)    
    if letras> n:
    
    i=0
    p=0
    
    while i<len(string):
        p= str.index(string, letra, n)
        i=p+1
        i+=1 
return p